def grade(n,k,v):
    table=[]
    print("STUDENT ID"+"    "+"MARKS")
    for a,b in zip(k,v):
        print(str(a)+"              "+str(b))
    v.sort()
    print(v)
    for i in range(100,0):
        i-=20
        index=0
        index=(i/100)*n
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
    
