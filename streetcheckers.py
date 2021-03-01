
def street_checkers(a,b):
    count=0
    case=0
    case+=1
    for i in range(a,b+1):
        alice=[]
        bob=[]
        diff=0
        tile_list=[]
        for j in range(1,b+1):
            if(j>i):
                break
            if(i%j==0):
               tile_list.append(j) 
        for x in tile_list:
            if(x%2!=0):
                alice.append(x)
            else:
                bob.append(x)
        diff=abs(len(alice)-len(bob))
        print(diff)
        if(diff<=2):
            count+=1
        else:
            pass
    print("case#"+str(case)+": "+str(count))

test_case=int(input())

for i in range(test_case):
    first=input().rstrip().split()
    l=int(first[0])
    r=int(first[1])
    result=street_checkers(l,r)
