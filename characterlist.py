



def maxchar(x):
    char=[]
    for i in range(0,len(x)):
        for j in range(i+1,len(x)):
            if(x[i]==x[j]):
                if(x[j]not in char):
                    char.append(x[j])
                else:
                    continue
    if(len(char)==1):
        return char[0]
    elif(len(char)==2)and(len(char)==0):
        return None
charlist=list(input().split(' '))
res=maxchar(charlist)

print(res)
