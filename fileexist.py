# file exitsts or not
# using isfile() method
# also import os module
import os
# using input function
fname=input('enter the file name: ')

if os.path.isfile(fname):
    print('file exist successfully')
else:
    print('file does not exit')
