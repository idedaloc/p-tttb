def master_yoda(n):
    return(n[::-1])

print("Testing master_yoda with master yoda")
print(master_yoda('master yoda'))

def laughter(pattern,text):
    c=0
    i=0
    while(pattern in text):
       c+=1
       text=text[text.index(pattern,i)+len(pattern):]
    return c

print("Testing laughter with hlhlssshlhl and hl")
print(laughter('hl','hlhlssshlhl'))
print("Testing laughter with hlhlssshlhl and s")
print(laughter('s','hlhlssshlhl'))
