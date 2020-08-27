# file in exclusive mode using 'x' mode
# if you are using 'x' mode file allready exist now showing fileExistError
# it create a new file and write data
with open('bac.txt','x') as f:
    f.write('comman man protection force')
print('file write successfully')