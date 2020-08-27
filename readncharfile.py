# read n character of file using read(n) method
# there is no exiting file  it showing FileNotFoundError
# file open using  'with'  function
with open('abc.txt','r') as f:
    print(f.read(10))
print('read 10 characters successfully')
