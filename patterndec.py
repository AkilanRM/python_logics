m=5
k=0
for row in range(k,m):
    for column in range(k,m):
        if(row==0)or(column==0):
            print(m,end=' ')
        elif(row==1)or(column==1):
            print(m-1,end=' ')
        elif(row==2)or(column==2):
            
            print(m-2,end=' ')
        elif(row==3)or(column==3):
            print(m-3,end=' ')
        else:
            print(m-4,end=' ')
    

    
    print(" ") 
            
        
