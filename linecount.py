with open('text.txt','r')as f:
    lcount=wcount=ccount=0
    for line in f :
        lcount=lcount+1
        word=line.split()
        wcount=wcount+len(word)
        ccount=ccount+len(line)
    print(lcount)
    print(wcount)
    print(ccount)

