import os
fname=input("enter filename :")
if os.path.isfile(fname):
    print('file exist ',fname)
    with open(fname,'r') as f:
        print(f.read())
else:
    print('file doesnot exit : ',fname)
