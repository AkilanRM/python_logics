def grade(n,k,v):
    table=[]
    print("STUDENT ID"+"    "+"MARKS")
    for a,b in zip(k,v):
        value=[]
        print(str(a)+"              "+str(b))
        value.append(a)
        value.append(b)
        table.append(value)
    print(table)
    v.sort()
    
    percent=100
    while(percent<0):
        percent-=20
        index=0
        index=i*n
        print(index)    
        
n=int(input())
k=[]
v=[]
for i in range(n):
    first=''
    first=input().split()
    x=int(first[0])
    y=int(first[1])
    k.append(x)
    v.append(y)
result=grade(n,k,v)
    
