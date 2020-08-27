# read line by line into list  using readlines() method
# file open using 'with' function,using mode is 'r' r means read mode
# There is no existing file it will showing FileNotFoundError
with open('abc.txt','r')as f:
    print(f.readlines())
print('read line by line into list successfully')