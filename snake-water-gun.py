import random
n=random.randint(1,3)
print('Welcome to the snake water game!')
if n==1:
    comp='s'
elif n==2:
    comp='w'
elif n==3:
    comp='g'
print('Please enter your input!\n For snake press: s\n For water press: w\n For gun press: g\n')
player=input()
if player=='s':
    if comp=='w':
        print('You win')
    elif comp=='g':
        print('You loose!')
    else:
        print("It's a draw!")

if player=='w':
    if comp=='w':
        print("It's a draw!")
    elif comp=='g':
        print('You loose!')
    else:
        print("You win!")

if player=='g':
    if comp=='w':
        print('You loose')
    elif comp=='g':
        print("It's a draw!")
    else:
        print("You loose!")



