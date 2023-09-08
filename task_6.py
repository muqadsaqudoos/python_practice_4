from random import *
row=4
col=3
a=[[randint(10,99) for i in range(col)]for j in range(row)]
for i in range(row):
    for j in range(col):
        print(a[i][j],end=' ')
print()
for i in range(row):
    sum=0
    for j in range(col):
        print(a[i][j],end=' ')
        sum+=a[i][j]
    print("=",sum)
