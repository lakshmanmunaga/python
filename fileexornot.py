import os
fname=input("enter the file name :")
if os.path.isfile(fname):
    print("the file name is :",fname)
else:
    print('file does not exit')