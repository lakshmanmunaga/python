import os
fname=input("enter the file name :")
if os.path.isfile(fname):
    # print file name
    print('file name is:',fname)
    # read file
    with open(fname,'r') as f:
        charcount=0
        for lines in f:
            charcount=charcount+len(lines)
        print(charcount)
else:
    print('file does not exists')