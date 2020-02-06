""" Guessing Game """
import random


def guessing_game():
    begin_number = 1
    end_number = 1000
    answer = random.randint(begin_number, end_number)  # generate a random integer from 1 to 1000
    guess_count = 0
    while True:
        try:
            guess_number = int(input(f"Enter your guess from {begin_number} to {end_number}: "))

            if begin_number > guess_number:
                print(f"Invalid number! {guess_number} less than {begin_number}")
                continue
            if guess_number > end_number:
                print(f"Invalid number! {guess_number} more than {end_number}")
                continue

            guess_count += 1

            if guess_number == answer:
                print(f"You got it! The hidden number is {answer}")
                print(f"It took you {guess_count} guess(es)")
                break
            else:
                print(f"Wrong! Guess count: {guess_count}")
                if guess_number > answer:
                    end_number = guess_number - 1
                else:
                    begin_number = guess_number + 1

        except ValueError as e:
            print("Please, input only digits!")


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()
