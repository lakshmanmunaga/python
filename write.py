# using write method if there is no existing file 'w' mode automatically created
# w mode using write file
# w mode is overwrite the data  exisiting file

with open('abc.txt','w') as f:
    f.write('why this is first line \n')
    f.write("why this is second line \n")
    f.write('this is third line')
print('file write successfully')
