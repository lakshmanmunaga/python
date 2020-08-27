# read file using read() method. it is read the entire file line by line
# it read existing file
# there is no exiting file it showing FileNotFoundError

with open('abc.txt','r')as f:
    print(f.read())
print('read file successfully')
