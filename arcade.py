import argparse
import sys
from numberguess import guessgame
from rps import rps

def gamechoose(name):

    while True:
        print("Please choose the game")
        print("1. Rock Paper Scissors")
        print("2. Guess the Number")

        print("")
        print("Or press x to exit the Arcade")
        print("")
        no=input()
        if no == '1':
            rps()
        elif no == '2':
            game=guessgame(name)
            game()
        elif no == 'x':
            print("See you next time")
            print()
            print(f"Bye {name}")
            sys.exit(0)
        else:
            print("Please enter a valid key")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Console games')
    parser.add_argument(
        '-n','--name',
        help='Enter your name',
        required=True
    )
    args = parser.parse_args()

    print(f"{args.name} Welcome to the Arcade")
    gamechoose(args.name)



