a=[1,2,4,5,7,9,11,15]
t= 8
for i in range(len(a)-1):
    if (a[i]==t):
        print(i)
    elif(a[i]>=t):
        print(i)
        break