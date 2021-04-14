from random import randint
import subprocess as sp

print("----------")
print("Welcome To Rock, Paper, Scissors!")
print("----------\n\n\n")




print("----------")
print("Which game do you want to play?")
print("1)Rock Paper Scissors\n2)Coinflip\n3)Number Guessing")
print("----------")

def rock_paper_scissors():
    a=1
    answer="y"
    while answer=="Y" or answer=="y":
        print("Select one of three!")
        print("----------")
        print("1. Rock\n2. Paper\n3. Scissors")
        print("----------")

        a=int(input())
        if a!=1 and a!=2 and a!=3:
            tmp = sp.call('cls', shell=True)
            print("\n\n")
            print("-----------------------------------------------------")
            print("Wrong input. Please select an option between 1 and 3")
            print("-----------------------------------------------------\n\n\n")
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
        tmp = sp.call('cls', shell=True)
        if answer=="n" or answer=="N":
            break

def Coinflip():
    answer="y"

    while answer=="Y" or answer=="y":
        print("Select one of two!")
        print("----------")
        print("1. Heads\n2. Tails\n")
        print("----------")

        option=int(input())

        if option!=1 and option!=2:
            tmp = sp.call('cls', shell=True)
            print("\n\n")
            print("-----------------------------------------------------")
            print("Wrong input. Please select an option between 1 and 3")
            print("-----------------------------------------------------\n\n\n")
            continue
        

        print("----------")
        print("Choosing...")
        print("----------")
        coin=randint(1,2)
        
        if option==1:
            if coin==1:
                print("Heads!\n\n")
                print("You Won!")
            elif coin==2:
                print("Tails!\n\n")
                print("You Lost!")
        elif option==2:
            if coin==1:
                print("Heads!\n\n")
                print("You Lost!")
            elif coin==2:
                print("Tails!\n\n")
                print("You Won!")
        print("Wanna play again? (Y/N)")
        answer=input()
        tmp = sp.call('cls', shell=True)
        if answer=="n" or answer=="N":
            break


d=int(input())

if d==1:
    rock_paper_scissors()
elif d==2:
    Coinflip()