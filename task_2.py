x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
sen=-1
y=[]
for i in range(len(x)):
    if x[i]!=sen:
        for j in range(i+1,len(x)):
            if x[i]==x[j]:
                x[j]=sen
        y.append(x[i])
print(y)


                
