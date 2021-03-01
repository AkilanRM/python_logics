def string(x):
    name=""
    number=''
    for i in x:
        if(i==':'):
            break
        else:
            name+=i
    invertx=x[::-1]
    length=str(len(name))
    for j in invertx:
        if(j==':'):
            break
        else:
            number+=j
    for k in number:
        if(k==length):
            return name[-1]
        else:
            return name[:2]
x=input()
result=string(x)
print(result)
