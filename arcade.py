import argparse
import sys

def gamechoose(name):
    print("Please choose the game")
    print("1. Rock Paper Scissors")
    print("2. Guess the Number")

    print("")
    print("Or press x to exit the Arcade")
    print("")

    while True:
        no=input()
        if no == '1':
            print('rps')
        elif no == '2':
            print('guess the number')
        elif no == 'x':
            print("See you next time")
            print()
            print(f"Bye {name}")
            sys.exit(0)
        else:
            print("Please enter a valid key")

if __file__ == '__main__':
    parser = argparse.ArgumentParser(description='Console games')
    parser.add_argument(
        '-n','--name',
        help='Enter your name',
        required=True
    )
    args = parser.parse_args()

    print(f"{args.name} Welcome to the Arcade")
    gamechoose(args.name)



