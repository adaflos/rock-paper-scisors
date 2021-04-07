from random import randint

print("----------")
print("Welcome To Rock, Paper, Scissors!")
print("----------")

answer="y"
a=1

while answer=="Y" or answer=="y":
    print("Select one of three!")
    print("----------")
    print("1. Rock\n2. Paper\n3. Scissors")
    print("----------")

    a=int(input())
    if a!=1 and a!=2 and a!=3:
        print("\n\n")
        print("----------")
        print("Wrong input. Please select an option between 1 and 3")
        print("----------\n\n\n")
        continue

    print("----------")
    print("Choosing...")
    print("----------")

    b=randint(1,3)

    if a==1:
        if b==1:
            print("Rock!\n\n")
            print("It's a Tie!")
        elif b==3:
            print("Scissors!\n\n")
            print("You Won!")
        elif b==2:
            print("Paper!\n\n")
            print("You Lost!")
    elif a==2:
        if b==2:
            print("Paper!\n\n")
            print("It's a Tie!")
        elif b==1:
            print("Rock!\n\n")
            print("You Won!")
        elif b==3:
            print("Scissors!\n\n")
            print("You Lost!")
    elif a==3:
        if b==3:
            print("Scissors!\n\n")
            print("It's a Tie!")
        elif b==2:
            print("Paper!\n\n")
            print("You Won!")
        elif b==1:
            print("Rock!\n\n")
            print("You Lost!")
    print("Wanna play again? (Y/N)")
    answer=input()
    if answer=="n" or answer=="N":
        break
