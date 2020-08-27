# How to count words in file
import os

fname = input('enter file name:')
if os.path.isfile(fname):
    print('file name is', fname)
    with open(fname, 'r')as f:
        wordcount = 0
        for line in f:
            word = line.split()
            wordcount = wordcount + len(word)
        print(wordcount)
else:
    print("file does not exits")