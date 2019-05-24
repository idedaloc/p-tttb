import random

def main():
    print('Guessing game')
    print('Guess a number between 1 and 100')
    m,c = start()
    if c == 0:
        print(m)
    else:
        print(m+' in '+str(c)+' tries')

def start():
    guess = -1
    c=0
    f=True
    rannum = random.randint(1,100)
    print(rannum)
    while True:
        n = input("Guess your number: ")
        if len(n) == 0:
            continue
        if f:
            if int(n) == rannum:
                return 'Out of bounds',c
            elif int(n) > rannum - 10 and int(n) < rannum + 10:
                print("WARM")
                guess = n
            else:
                print("Cold")
                guess = n
        else:
            if int(n) == rannum:
                return 'Number guessed',c
            elif abs(int(n)-rannum) < abs(int(guess)-rannum):
                print("Warmer")
                guess = n
            else:
                print("Colder")
                guess = n
        c+=1
        f=False
main()
