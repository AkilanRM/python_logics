def maximal(n,chairs):
    
    for i in range(0,n):
        if(chairs[0]==1):
            if(chairs[1]==0):
                pass
            else:
                return "no"
        elif(chairs[n-1]==1):
            if(chairs[n-2]==0):
               pass
            else:
                return "no"
        elif(chairs[i]==1):
            a=chairs[i-1]
            b=chairs[i+1]
            if(a==0 and b==0):
                pass
            else:
                return "no"
    return "yes"

chairs=[]
n=int(input())
for i in range(0,n):
    chairs.append(int(input()))
result=maximal(n,chairs)
