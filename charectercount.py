import os
fname=input('enter file name:')
if os.path.isfile(fname):
    print('exists file is :',fname)
    with open(fname,'r') as f:
     ccount=0
     for char in f:
        ccount=ccount+len(char)
     print(ccount)
else:
    print('file does not exist',fname)
