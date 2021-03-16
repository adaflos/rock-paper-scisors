from random import randint

print("----------")
print("Welcome To Rock, Paper, Scisors!")
print("----------")

print("Select one of three!")
print("----------")

print("1. Rock\n2. Paper\n3. Scisors")
print("----------")

a=int(input())
print("----------")

print("Choosing...")
print("----------")

b=randint(1,3)

if a==1:
    if b==1:
        print("Rock!\n\n")
        print("It's a Tie!")
    elif b==3:
        print("Paper!\n\n")
        print("You Won!")
    elif b==2:
        print("Scisors!\n\n")
        print("You Lost!")
elif a==2:
    if b==2:
        print("Paper!\n\n")
        print("It's a Tie!")
    elif b==1:
        print("Rock!\n\n")
        print("You Won!")
    elif b==3:
        print("Scisors!\n\n")
        print("You Lost!")
elif a==3:
    if b==3:
        print("Scisors!\n\n")
        print("It's a Tie!")
    elif b==2:
        print("Paper!\n\n")
        print("You Won!")
    elif b==1:
        print("Rock!\n\n")
        print("You Lost!")

input()