def sn(a,t):
    b=[]
    for x in a:
        y=''
        z=''
        y+=x[:1]
        z+=x[1:]
        b.append(int(z+y))
    if(t=='a'):
        b.sort()
        return b
    else:
        b.sort(reverse=True)
        return b
        
n=int(input())
list_3=[]
t=input()
for i in range(n):
    list_3.append(input())
result=sn(list_3,t)
print(result)
