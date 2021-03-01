result=[]
element=[]
for i in range(0,5):
    element+=[int(input())]
n=len(element)
for x in range(0,n+1):
    y=max(element)
    if(element[x]>y):
        element.pop(x)
        result+=[y]
    else:
        element.pop(x)
        result+=['-1']
        
        
    
