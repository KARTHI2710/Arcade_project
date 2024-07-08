from random import choice

count = 0
win=0
def guessgame(name):
    
    while True:
        print(f"{name}, guess which number I'm thinking of 1,2 and 3.")
        print()
        no=(input())
        print()
        computer=choice("123")
        if no == computer:
            pass
            count=count+1
            win=win+1
        else:
            print(f"{name}, you chose {no}")
            print(f"I was thinking about the number {computer}")
            print()
            print(f"sorry {name} Better Luck next Time !!! ")
            count=count+1

        print(f'Game count : {count}')
        print(f'{name}\'s wins : {win}')
        print(f'Your winning percentage : {count * win / 100}%')
        print("")
        print(f"Play again {name}?")
        print("")
        print('Y for yes or N for no')
        ans=input()

        if ans == 'Y':
            pass
        elif ans == 'N':
            print('Thank you for playing')
            return
        else:
            print('Please enter a valid key')


