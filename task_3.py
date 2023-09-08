x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
y=[x[i] for i in range(len(x))]
Y=[]
C=[]
sen=-1
for i in range(len(x)):
    if x[i]!=sen:
        for j in range(i+1,len(x)):
            if x[i]==x[j]:
                x[j]=sen
        Y.append(x[i])
print(Y)
for i in range(len(y)):
    count=1
    if x[i]!=sen:
        for j in range(i+1,len(y)):
            if y[i]==y[j]:
                count+=1
                y[j]=sen
        C.append(count)
print(C)
