x_list = list(map(int, input("Enter a multiple value: ").split()))
new_list=[]
new1_list=[]
result_list=[]
for i in range(0,len(x_list)):
    
    
    if((i%2)==0):
        new_list+=[x_list[i]]
        new_list.sort(reverse=True)
    elif((i%2)!=0):
        new1_list+=[x_list[i]]
        new1_list.sort()
       
print(new_list,new1_list)
for x,y in zip(new_list,new1_list):
    result_list.append(x)
    result_list.append(y)
print(result_list)
