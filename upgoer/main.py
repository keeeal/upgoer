
from argparse import ArgumentParser
from pathlib import Path
from random import choice

from numpy.linalg import norm
from seaborn import histplot
from termcolor import colored

from utils.data import clean_word, load_words, load_vectors


def main(words_path: Path, vectors_path: Path):
    words = load_words(words_path)
    vectors = load_vectors(vectors_path)
    words = [word for word in words if word in vectors]

    test = """
Hi James, thanks for taking the time to leave an honest, impartial and fair review. You can get any of our menu Burgers in vegetarian form, by either replacing the all beef patty with an awesome vegetarian patty, or our extremely popular hash brown option which gives you two golden hash browns with melted cheese.

We don't have any surcharge for this option (unlike many other eateries) which means you can get a Vegetarian Cheeseburger for $8 or a vegetarian Single $10 (which includes fresh crisp lettuce, juicy tomato, onion, cheese, secret sauce all on freshly toasted bun). Personally, we think that's pretty decent value, but hey, 6 years of successful trade, what do we know!

All the best with your next dining experience, hopefully you find something that suits your price point BEFORE you order, so that you aren't forced to leave your welcome review.
"""

    def distance(a: str, b: str) -> float:
        return float(norm(vectors[a] - vectors[b]))

    def closest_word(word: str) -> tuple[str, float]:
        word = clean_word(word)
        if word not in vectors:
            return "🎲" + choice(list(words)) + "🎲", 999
        closest = min(words, key=lambda w: distance(w, word))
        return closest, distance(closest, word)

    def color_word(x: tuple[str, float]) -> str:
        word, value = x
        if value == 0:
            return word
        elif value < 3:
            c = "cyan"
        elif value < 3.5:
            c = "blue"
        elif value < 4:
            c = "green"
        elif value < 4.5:
            c = "yellow"
        elif value < 5:
            c = "magenta"
        else:
            c = "red"

        return colored(word, c)

    output = [closest_word(word) for word in test.split()]
    print(" ".join(map(color_word, output)))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-w", "--words-path", type=Path, default="data/1000.txt")
    parser.add_argument("-v", "--vectors-path", type=Path, default="data/glove.6B/glove.6B.50d.txt")
    main(**vars(parser.parse_args()))
