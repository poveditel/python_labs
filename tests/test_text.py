import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


class TestNormalize:
    @pytest.mark.parametrize(
        "source, expected",
        [
            ("ПрИвЕт\nМИр\t", "привет мир"),
            ("ёжик, Ёлка", "ежик, елка"),
            ("Hello\r\nWorld", "hello world"),
            ("  двойные   пробелы  ", "двойные пробелы"),
            ("", ""),  # пустая строка
            ("   ", ""),  # только пробелы
            ("\n\t\r   ", ""),  # управляющие символы и пробелы
            (
                "Съешь ещё этих мягких французских булок",
                "съешь еще этих мягких французских булок",
            ),
        ],
    )
    def test_normalize(self, source, expected):
        assert normalize(source) == expected

    def test_normalize_preserves_punctuation(self):
        text = "Привет, мир! Как дела?"
        result = normalize(text)
        assert "привет, мир! как дела?" == result


class TestTokenize:
    @pytest.mark.parametrize(
        "source, expected",
        [
            ("привет мир", ["привет", "мир"]),
            ("Hello World", ["hello", "world"]),
            ("раз-два-три", ["раз", "два", "три"]),
            ("", []),  # пустая строка
            ("!!! ??? ...", []),  # только пунктуация
            ("word1 word2 word3", ["word1", "word2", "word3"]),
            ("Он сказал: 'Привет!'", ["он", "сказал", "привет"]),
        ],
    )
    def test_tokenize(self, source, expected):
        assert tokenize(source) == expected

    def test_tokenize_case_insensitive(self):
        text = "Привет МИР Hello WORLD"
        result = tokenize(text)
        assert result == ["привет", "мир", "hello", "world"]


class TestCountFreq:
    def test_count_freq_basic(self):
        tokens = ["я", "люблю", "python", "python", "люблю", "я", "я"]
        result = count_freq(tokens)
        expected = {"я": 3, "люблю": 2, "python": 2}
        assert result == expected

        assert count_freq([]) == {}

    def test_count_freq_single(self):
        assert count_freq(["слово"]) == {"слово": 1}

    def test_count_freq_special_chars(self):
        tokens = ["word", "word", "word2", "word2", "word2"]
        result = count_freq(tokens)
        assert result["word"] == 2
        assert result["word2"] == 3


class TestTopN:
    def test_top_n_basic(self):
        freq = {"я": 5, "ты": 3, "он": 7, "она": 2}
        result = top_n(freq, 3)
        expected = [("он", 7), ("я", 5), ("ты", 3)]
        assert result == expected

    def test_top_n_tie_breaker(self):
        freq = {"яблоко": 3, "апельсин": 3, "банан": 3, "груша": 2}
        result = top_n(freq, 3)
        expected = [("апельсин", 3), ("банан", 3), ("яблоко", 3)]
        assert result == expected

    def test_top_n_more_than_available(self):
        freq = {"а": 1, "б": 2}
        result = top_n(freq, 10)
        assert len(result) == 2
        assert result == [("б", 2), ("а", 1)]

    def test_top_n_empty_dict(self):
        assert top_n({}, 5) == []

    def test_top_n_zero_n(self):
        freq = {"а": 1, "б": 2}
        assert top_n(freq, 0) == []

    def test_top_n_negative_n(self):
        freq = {"а": 1, "б": 2}
        assert top_n(freq, -1) == []


class TestIntegration:
    def test_full_pipeline(self):
        text = "Привет мир! Привет всем. Мир прекрасен."

        normalized = normalize(text)
        assert normalized == "привет мир! привет всем. мир прекрасен."

        tokens = tokenize(normalized)
        assert tokens == ["привет", "мир", "привет", "всем", "мир", "прекрасен"]

        freq = count_freq(tokens)
        expected_freq = {"привет": 2, "мир": 2, "всем": 1, "прекрасен": 1}
        assert freq == expected_freq

        top = top_n(freq, 2)
        # При равенстве частот сортировка по алфавиту: "мир", потом "привет"
        assert top == [("мир", 2), ("привет", 2)]
