from random import *
rows=4
col=4
a=[[randint(10,99)for j in range(col)] for i in range(rows)]
for i in  range(rows):
    for j in range(col):
        print(a[i][j],end=' ')
print()
print("princial diagonal:",end=' ')
for i in range(rows):
    for j in range(col):
        if i==j:
            print(a[i][j],end= ' ')
print()
print('secondary digonal:',end=' ')
b=rows
for i in range(rows):
    for j in range(col):
        if j==b-1:
            print(a[i][j],end=' ')
            b-=1


