import random

def guess_the_number():
    digit = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < digit:
            print("Больше!")
        elif guess > digit:
            print("Меньше!")
        else:
            print(f"Вы угадали число {guess} за {attempts} попыток.")
            break

if __name__ == "__main__":
    guess_the_number()

