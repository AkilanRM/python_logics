even=2
odd=7
k=0
q=0
res=1
n=int(input())
for i in range(n):
    for j in range(n):
        if i>=j:
            print(res,end="")
    res+=1
    print(" ")
