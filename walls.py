walls=int(input())
height=[]
count=1
x=1
for i in range(walls):
    height.append(int(input()))
for j in range(0,walls):
    k=j+1
    if(j==walls-1):
        break
    elif(height[j] < height[k]):
       count+=1
    else:
       pass
    k+=1
    
print(count)    
