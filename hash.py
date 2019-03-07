from time import time
from hashlib import sha256


def get_word(hash, file, symbols):
    start = time()

    for w in file:
        for s1 in symbols:
            for s2 in symbols:
                guess = s1 + w + s2
                guess_hash = sha256(guess.encode()).hexdigest()
                if hash == guess_hash:
                    end = time()
                    return guess, end - start


file = open("words.txt", "r", encoding='utf-8')
hash = "b1435b304bf50e05853947ea8c0b5f19ac26bf5f8c8fe5f927b4a744c2443232"
symbols = list("!$%&/()=?")

file = [line.strip("\r\n") for line in file]

word, taken_time = get_word(hash, file, symbols)

print("%s - %fs" % (word, taken_time))
