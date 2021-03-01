m=5
n=5
for i in range(m):
    for j in range(n):
        if(i<=2):
            if(i==j):
                print('*',end="  ")
            elif(i+j==4):
                print('*',end=" ")
        if(i>2) and (i<=4):
            if(j==2):
                print('*',end="  ")
    print(" ")
