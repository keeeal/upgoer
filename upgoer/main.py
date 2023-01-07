
from argparse import ArgumentParser
from pathlib import Path

from utils.data import load_words


def main(words: Path):
    print(load_words(words))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-w", "--words", type=Path, default="data/1000.txt")
    main(**vars(parser.parse_args()))
