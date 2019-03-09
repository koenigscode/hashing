"""
Task: With a SHA256 hash given find out the password consisting of two words and a special character (!$%&/()=?)
The words are provided in words.txt
"""

from time import time
from hashlib import sha256

HASH = "b1435b304bf50e05853947ea8c0b5f19ac26bf5f8c8fe5f927b4a744c2443232"
SYMBOLS = list("!$%&/()=?")
WORDS_FILE = "words.txt"


def get_word(hash: str, filename: str, symbols: list) -> (str, str):
    """
    finds the plain text form of a hash consisting of two words,
    one symbol at the beginning and one at the end
        :param hash: sha256 hash of the password
        :param file: file containing possible words of the password
        :param symbols: possible symbols at the beginning and end of the password
    """

    words_file = open(filename, "r", encoding='utf-8')
    words = [line.strip("\r\n") for line in words_file]
    words_file.close()

    start = time()

    for w in words:
        for s1 in symbols:
            for s2 in symbols:
                guess = s1 + w + s2
                guess_hash = sha256(guess.encode()).hexdigest()
                if hash == guess_hash:
                    end = time()
                    return guess, end - start


if __name__ == "__main__":
    word, time_taken = get_word(HASH, WORDS_FILE, SYMBOLS)
    print(f"{word} - {time_taken}s")
