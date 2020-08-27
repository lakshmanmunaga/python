# If your add data to file  then using file append mode 'a'
#using 'a' append mode add the data at the ending of  file
# open file using with function
with open('abc.txt','a')as f:
    f.write('i have a long hair')
    f.write('i dont have a pencil')
print('add data successfully')
