
from random import *
col=3
rows=4
a=[[randint(10,99) for i in range(col)] for j in range(rows)]
for i in range(rows):
    for j in range(col):
        print(a[i][j],end = ' ')
print()
print()
for i in range(rows):
    for j in range(col):
        print(a[i][j],end=' ')
    print()
print()
count=0
for i in range(rows):
    for j in range(col):
        print(a[i][j],end=' ')
        count+=1
        if count==rows:
            print()
            count=0
        

