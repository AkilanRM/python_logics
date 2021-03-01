def numbers_2_billion(n):
    ans=[]
    lst=[]
    flag=0
    for x in n:
        lst.append(x)
    change=['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens=['zero','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    value=['hundred','thousand','million','billion']
    final=''
    two=0
    while(len(lst)>0):
        val=''
        val2=''
        val1=''
        result=''
        flag+=1
        val=lst.pop()
        for i in range(0,len(change)):
            if(int(val)==i)and(len(lst)==0):
                result+=(change[i])
                ans.insert(0,result)
            elif(int(val)==i):
                val1=lst.pop()
                x=int(val1+val)
                if(x<20):
                    result+=change[x]
                    ans.insert(0,result)
                else:
                    for j in range(0,len(tens)):
                        if(int(val1)==j)and(int(val)!=0):
                            result+=(tens[j]+' '+change[i])
                            ans.insert(0,result)
                        elif(int(val1)==j):
                            result+=tens[j]
                            ans.insert(0,result)
        if(len(lst)==0):
            two=1
            break
        else:
            val2=lst.pop()
            for i in range(0,len(change)):
                if(int(val2)==i):
                    ans.insert(0,change[i])
                    ans.insert(1,value[0])
    if(flag==1):
        pass
    elif(flag==2):
        if(two==0):
            ans.insert(3,value[1])
        else:
            ans.insert(1,value[1])
    elif(flag==3):
        if(two==0):
            ans.insert(3,value[2])
            ans.insert(7,value[1])
        else:
            ans.insert(1,value[2])
            ans.insert(5,value[1])
    else:
        if(two==0):
            ans.insert(3,value[3])
            ans.insert(7,value[2])
            ans.insert(11,value[1])
        else:
            ans.insert(1,value[3])
            ans.insert(5,value[2])
            ans.insert(9,value[1])
    for word in range(0,len(ans)):
        if(word==0):
            final+=ans[word]
            final+=" "
        elif(ans[word]=="zero"):
            continue
        elif(ans[word]==value[0])and (ans[word-1]=="zero"):
            continue
        else:
            final+=ans[word]
            final+=" "
    return final
n=input("enter the value :")
res=numbers_2_billion(n)
print(res)
