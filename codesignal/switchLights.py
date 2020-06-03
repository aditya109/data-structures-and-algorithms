def switchLights(a):
    for i in range(len(a)):
        if a[i] == 1 and i!= 0:
            a[i]=a[i]^1
            for j in range(i):
                a[j]=a[j+1]^1
        elif a[i]==1 and i==0:
            a[i]=a[i]^1
        print(a)
        
    return a
print(switchLights([1, 1, 1, 1, 1]))