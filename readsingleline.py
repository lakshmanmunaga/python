# read single line using readline() method
# There is no exiting file it will showing FileNotFoundError
# file open using 'with' function
with open('abc.txt','r')as f:
    print(f.readline())
print('readline successfully')