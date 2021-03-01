def addnum(x):
    strt=x.index("5")
    end=x.index("8")
    midnum=(x[strt:end+1])
    print(midnum)
    num=" "
    count=0
    for i in x:
        if(i in midnum):
            continue
        else:
            num+=i
    print(num)
    num=int(num)
    while(num>0):
        n=num%10
        count+=n
        num=num//10
    midnum=int(midnum)
    return midnum+count
        
x=input()
result=addnum(x)
print(result)






