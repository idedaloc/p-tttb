def print3t(**kwargs):
    for p in range(9):
        if p != 0 and p % 3 == 0:
            print('\n------')
        print(('O' if p in kwargs['O'] else ('X' if p in kwargs['X'] else str(p))) + '|', end='')
    else:
        print('\n')

def evaluateH(**kwargs):
    e = set() 
    for p in range(9):
        if p != 0 and p % 3 == 0:
            if len(e) == 1:
                return e.pop()
            else: 
                e = set()
        e.add('O' if p in kwargs['O'] else ('X' if p in kwargs['X'] else '-1'))
    else:
        return -1



def evaluateV(**kwargs):
    for o in range(3):
        if o in kwargs['O'] and o + 3 in kwargs['O'] and o + 6 in kwargs['O']:
            return 'O'
    for x in range(3):
        if x in kwargs['X'] and x + 3 in kwargs['X'] and x + 6 in kwargs['X']:
            return 'X'
    return -1
    


def evaluateD(**kwargs):
    if ( 4 in kwargs['O'] ) and (( 0 in kwargs['O'] and 8 in kwargs['O'] ) or ( 2 in kwargs['O'] and 6 in kwargs['O'] )):
        return 'O'
    if ( 4 in kwargs['X'] ) and (( 0 in kwargs['X'] and 8 in kwargs['X'] ) or ( 2 in kwargs['X'] and 6 in kwargs['X'] )):
        return 'X'
    return -1

def mainT(o,x):
    print3t(O=o,X=x) 
    print(evaluateH(O=o,X=x))
    print(evaluateV(O=o,X=x))
    print(evaluateD(O=o,X=x))

def main():
    o=[]
    x=[]

    turn='x'

    print("TIC-TAC-TOE\n\n")

    while True:
        print(o,x)
        print3t(O=o,X=x)

        if(turn == 'x'):
            ix = input('X turn: ')
            if len(str(ix))==0 or not int(ix) in range(9) or int(ix) in o+x:
                print('Bad option')
                turn='x'
                continue
            x.append(int(ix))
            turn = 'o'
        else:
            io = input('O turn: ')
            if len(str(io))==0 or not int(io) in range(9) or int(io) in o+x:
                print('Bad option')
                turn='o'
                continue
            o.append(int(io))
            turn = 'x'

        if(evaluateH(O=o,X=x) == 'X'):
            print('\nX win')
            print3t(O=o,X=x)
            break
        if(evaluateH(O=o,X=x) == 'O'):
            print('\nO win')
            print3t(O=o,X=x)
            break
        if(evaluateV(O=o,X=x) == 'X'):
            print('\nX win')
            print3t(O=o,X=x)
            break
        if(evaluateV(O=o,X=x) == 'O'):
            print('\nO win')
            print3t(O=o,X=x)
            break
        if(evaluateD(O=o,X=x) == 'X'):
            print('\nX win')
            print3t(O=o,X=x)
            break
        if(evaluateD(O=o,X=x) == 'O'):
            print('\nO win')
            print3t(O=o,X=x)
            break

        if len(o+x) == 9:
            print('\nGato')
            print3t(O=o,X=x)
            break

#mainT([],[0,1,2])
main()       
