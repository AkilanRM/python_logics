
def palindrome(x):       
    count=0
    flag=0
    while(flag!=1):
        bits=bin(x)
        val=bits[2:]
        print(val)
        val1=val[::-1]
        print(val1)

    
        if(val==val1):
            print("THESE BITS ARE PALINDROME OF :"+str(x))
            return count
            flag=1
            break
        else:
            x=x+1
            count+=1

x=int(input())
result=palindrome(x)
print(result)
