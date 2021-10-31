import os

fn = "book.txt"
file = open(fn, 'r')
ch = 0
wrds = 0
for line in file:
    line = line.strip(os.linesep)
    wordslist = line.split()
    wrds = wrds + len(wordslist)
    ch = ch + len(line)
    sp = wrds - 1
print("Characters:", ch, "\nSpaces:", sp, "\nWords:", wrds)

