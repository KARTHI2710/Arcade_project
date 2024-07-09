from random import choice

def choices(arg):
    math_dict={
        "1":"Rock",
        "2":"Paper",
        "3":"Scissors"
    }
    return math_dict[arg]

def rps():
    while True:
        print("")
        print("Enter you choice")
        print("")

        print("1.Rock")
        print("2.Paper")
        print("3.Scissors")

        print("")
        no=input()
        print("")

        print(f"You chose {choices(no)}")
        computer=choice("123")
        print(f"Computer chose {choices(computer)}")

        if choices(no) == choices(computer):
            print("Match Tie")
        elif choices(no) == 'Rock' and choices(computer) == 'Scissors':
            print("You win")
        elif choices(no) == 'Paper' and choices(computer) == 'Rock':
            print("You win")
        elif choices(no) == 'Scissors' and choices(computer) == 'Paper':
            print("You win")
        else:
            print("Computer win")

        print("")
        print("Do you want to play the again? if 'yes' enter Y otherwise enter N")
        print("")
        
        while True:
            decision=input()
            if decision == 'Y':
                break
            elif decision == 'N':
                return
            else:
                print("Enter a valid key")
