""" Game to guess the number """
import random


def generate_random_number(start: int, end: int) -> int:
    """Function to generate random number that user has to guess"""
    return random.randint(start,end)


def check_number(user_number: int, app_number: int):
    """ Checks number whether it's bigger or not"""
    if user_number > app_number:
        print("A little bit too much")
    elif user_number < app_number:
        print("A little bit more")


def user_input(prompt: str) -> str:
    """Gets user input"""
    while True:
        try:
            user_guess = int(input(prompt))
            if 1 <= user_guess <= 10:
                return user_guess
            print("The number is  out of range")
        except ValueError:
            print("INCORRECT INPUT, ONLY INTEGERS ALLOWED!")


def main():
    """Main function"""
    random_number = generate_random_number(1, 10)
    print("Welcome to our game! Try to guess the number!")

    while True:
        user_guess = user_input("Number is (from 1 to 10):")
        try:
            if user_guess == random_number:
                print("YOU WON! THE NUMBER IS = " + str(random_number))
                break
            check_number(user_guess, random_number)
        except ValueError:
            print("WRONG NUMBER! TRY ONE MORE TIME!")


if __name__ == "__main__":
    main()
