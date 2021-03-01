import math
def kaprekarNumber(n,m):
    
    for i in range(n,m+1):
        square=1
        r=' '
        l=' '
        square=i*i
        print(square)
        x=str(square)
        half=len(x)/2
        if(type(half)==float):
            y=math.ceil(half)
        else:
            y=half
        l+=x[0,y]
        r+=x[y,len(x)]
        result=int(l)+int(r)
        if(result==i):
            print(result,"it is a kaprekarNumber")
        else:
            continue
        
            
n=int(input())
m=int(input())
result=kaprekarNumber(n,m)

