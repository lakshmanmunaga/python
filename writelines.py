with open('text.txt','w') as f:
    list=['iam boy\n','i have bed\n','i was great\n']
    f.writelines(list)
    print('written success')


f1=open('text.txt','r')
print(f1.read())


