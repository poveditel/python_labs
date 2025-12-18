from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                f"Invalid birthdate format: {self.birthdate}. Expected format: YYYY-MM-DD"
            )

        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA must be between 0 and 5, got: {self.gpa}")

    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year
        if today.month < birth_date.month or (
            today.month == birth_date.month and today.day < birth_date.day
        ):
            age -= 1
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

    def __str__(self):
        return f"Student: {self.fio}, Group: {self.group}, GPA: {self.gpa}, Age: {self.age()}"


if __name__ == "__main__":
    student = Student("Ivanov Ivan Ivanovich", "2000-05-15", "SE-01", 4.2)
    print(student)
    print(f"Age: {student.age()}")

    student_dict = student.to_dict()
    print(f"Serialized: {student_dict}")

    restored_student = Student.from_dict(student_dict)
    print(f"Restored: {restored_student}")
