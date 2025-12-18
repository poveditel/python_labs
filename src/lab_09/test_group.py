import tempfile
import json
from pathlib import Path
import pytest
from src.lab_08.models import Student
from src.lab_09.group import Group


class TestGroup:
    @pytest.fixture
    def temp_file(self):
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".csv", delete=False, encoding="utf-8"
        ) as f:
            f.write("fio,birthdate,group,gpa\n")
            f.write("Иванов Иван Иванович,2000-01-15,ИСТ-201,4.5\n")
            f.write("Петров Петр Петрович,2001-03-20,ИСТ-201,3.8\n")
            f.write("Сидорова Анна Сергеевна,2000-12-05,ИСТ-202,4.9\n")
        yield f.name
        Path(f.name).unlink(missing_ok=True)

    @pytest.fixture
    def group(self, temp_file):
        return Group(temp_file)

    @pytest.fixture
    def new_student(self):
        return Student(
            fio="Новый Студент Тестовый",
            birthdate="2002-06-30",
            group="ИСТ-203",
            gpa=4.2,
        )

    def test_init_creates_file_if_not_exists(self):
        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
            temp_path = f.name

        Path(temp_path).unlink()

        group = Group(temp_path)
        assert group.path.exists()
        assert group.path.suffix == ".csv"

        with open(temp_path, "r", encoding="utf-8") as f:
            content = f.read()
            assert "fio,birthdate,group,gpa" in content

        Path(temp_path).unlink()

    def test_list_returns_all_students(self, group):
        students = group.list()

        assert len(students) == 3
        assert isinstance(students[0], Student)
        assert students[0].fio == "Иванов Иван Иванович"
        assert students[0].gpa == 4.5
        assert students[1].fio == "Петров Петр Петрович"
        assert students[2].fio == "Сидорова Анна Сергеевна"

    def test_list_handles_invalid_records(self, temp_file):
        with open(temp_file, "a", encoding="utf-8") as f:
            f.write("Невалидный Студент,not-a-date,ИСТ-201,not-a-float\n")

        group = Group(temp_file)
        students = group.list()

        assert len(students) == 3

    def test_add_student(self, group, new_student):
        initial_count = len(group.list())

        group.add(new_student)
        students = group.list()

        assert len(students) == initial_count + 1
        assert students[-1].fio == new_student.fio
        assert students[-1].group == new_student.group
        assert students[-1].gpa == new_student.gpa

    def test_remove_student(self, group):
        initial_count = len(group.list())

        removed_count = group.remove("Иванов Иван Иванович")
        assert removed_count == 1

        students = group.list()
        assert len(students) == initial_count - 1
        assert all(s.fio != "Иванов Иван Иванович" for s in students)

        removed_count = group.remove("Несуществующий Студент")
        assert removed_count == 0

    def test_update_student(self, group):
        updated = group.update("Иванов Иван Иванович", gpa=5.0, group="ИСТ-301")
        assert updated is True

        students = group.list()
        updated_student = next(s for s in students if s.fio == "Иванов Иван Иванович")
        assert updated_student.gpa == 5.0
        assert updated_student.group == "ИСТ-301"

        updated = group.update("Несуществующий Студент", gpa=1.0)
        assert updated is False

    def test_update_partial_fields(self, group):
        updated = group.update("Петров Петр Петрович", gpa=4.0)
        assert updated is True

        students = group.list()
        updated_student = next(s for s in students if s.fio == "Петров Петр Петрович")
        assert updated_student.gpa == 4.0
        assert updated_student.birthdate == "2001-03-20"
        assert updated_student.group == "ИСТ-201"

    def test_stats_empty_group(self):
        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
            temp_path = f.name

        with open(temp_path, "w", encoding="utf-8") as f:
            f.write("fio,birthdate,group,gpa\n")

        group = Group(temp_path)
        stats = group.stats()

        assert stats["count"] == 0
        assert stats["min_gpa"] is None
        assert stats["max_gpa"] is None
        assert stats["avg_gpa"] is None
        assert stats["groups"] == {}
        assert stats["top_5_students"] == []

        Path(temp_path).unlink()

    def test_stats_non_empty_group(self, group):
        stats = group.stats()

        assert stats["count"] == 3
        assert stats["min_gpa"] == 3.8
        assert stats["max_gpa"] == 4.9
        assert stats["avg_gpa"] == round((4.5 + 3.8 + 4.9) / 3, 2)

        assert stats["groups"] == {"ИСТ-201": 2, "ИСТ-202": 1}

        assert len(stats["top_5_students"]) == 3
        assert stats["top_5_students"][0]["fio"] == "Сидорова Анна Сергеевна"
        assert stats["top_5_students"][0]["gpa"] == 4.9
        assert stats["top_5_students"][1]["gpa"] == 4.5
        assert stats["top_5_students"][2]["gpa"] == 3.8

    def test_export_to_json(self, group, temp_file):
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
            json_path = f.name

        group.export_to_json(json_path)

        assert Path(json_path).exists()

        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert isinstance(data, list)
        assert len(data) == 3
        assert data[0]["fio"] == "Иванов Иван Иванович"
        assert float(data[0]["gpa"]) == 4.5

        Path(json_path).unlink()

    def test_write_all_preserves_order(self, group, new_student):
        original_students = group.list()
        original_fios = [s.fio for s in original_students]

        group.add(new_student)

        updated_students = group.list()
        updated_fios = [s.fio for s in updated_students]

        assert updated_fios[:-1] == original_fios
        assert updated_fios[-1] == new_student.fio

    def test_multiple_operations(self, group):
        initial_count = len(group.list())

        new_student = Student(
            fio="Тестовый Студент", birthdate="2003-01-01", group="ИСТ-203", gpa=3.5
        )
        group.add(new_student)
        assert len(group.list()) == initial_count + 1

        group.update("Тестовый Студент", gpa=4.0)
        updated = next(s for s in group.list() if s.fio == "Тестовый Студент")
        assert updated.gpa == 4.0

        removed = group.remove("Тестовый Студент")
        assert removed == 1
        assert len(group.list()) == initial_count

        remaining_fios = [s.fio for s in group.list()]
        assert "Иванов Иван Иванович" in remaining_fios
        assert "Тестовый Студент" not in remaining_fios


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
