# write multiple lines in file
# using writelines() method
#open file using with function

with open('adc.txt','w') as f:
    list=['this is yhehav grammaer lecture\n','this is also atale of story \n','i dont have grammer knoweldge']
    f.writelines(list)
print('write file successfully')