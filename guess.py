from random import randint
answer = randint(1, 6)

while True:
    try:
        num = input('guess the number:  ')
        if int(num) > 0 and int(num) < 7:
            if int(answer) == int(num):
                print('you are genius')
                break
        else:
            print('enter number 1 to 6')
    except ValueError:
        print('hey i said number')
        continue
