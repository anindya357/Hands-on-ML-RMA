from random import randint
from time import time


MAX = 50
MIN = 20


def game():
    a = randint(MIN, MAX)
    b = randint(MIN, MAX)

    total = a + b

    print("Try to add these numbers ASAP.")
    print(f"{a} + {b} = ?")
    display_time = time()

    answer = int(input("My answer: "))
    input_time = time()

    correct = total == answer
    elapsed = input_time - display_time

    print(f"RESULT: {correct}")
    print(f"Time elapsed: {elapsed:.3} seconds")


if __name__ == "__main__":
    game()

