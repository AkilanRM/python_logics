def candies(a,n):
    good=0
    for x in range(n):
        val=a.pop(x)
        odd=0
        even=0
    
        for wigh in range(0,len(a)):
            
            if(wigh%2==0):
                odd+=a[wigh]
            else:
                even+=a[wigh]
        print(str(odd)+" "+str(even))
        a.insert(x,val)
        if(odd!=even):
            continue
        else:
            good+=1
    return good
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
res=candies(a,n)
print(res)
