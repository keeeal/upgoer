
from pathlib import Path

from numpy import array, ndarray


def clean_word(word: str) -> str:
    return "".join(filter(str.islower, word.lower().strip()))


def load_words(path: Path | str) -> list[str]:
    with open(path) as f:
        return list(map(clean_word, f.readlines()))


def load_vectors(path: Path | str) -> dict[str, ndarray[float]]:
    def read_vector(line: str) -> tuple[str, ndarray[float]]:
        word, *vector = line.split()
        return clean_word(word), array(list(map(float, vector)))

    with open(path) as f:
        vectors = dict(map(read_vector, f.readlines()))

    del vectors[""]
    return vectors

