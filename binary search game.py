n=45
i=1
for i in range(1,10):
    print('You have',10-i,'number of chances left')
    a = int(input('Guess the number'))
    if a>n:
        print('Number entered is greater then the actual one')
    elif a<n:
        print('Number entered is less then the actual one')
    else:
        print('Congratulations you have entered the right number')
        break
    i=i+1
    if i>9:
        print('Game over')
        break