def minimumSugar(a,b,c,d):
    d+=1
    bd=1
    rd=2
    comp_list=[]
    total_list=[]
    count=0
    if(a==2):
        if(b==bd):
            print("case#"+str(d)+": "+str(bd))            
        else:
            print("case#"+str(d)+": "+str(rd)) 
    elif(a>2):
        for x in c:
            for y in x:
                comp_list.append(y)
                continue
        total_list.append(comp_list)
        for p in range(1,a+1):
            check_list=[]
            if(p==a):
                break
            check_list.append(str(p))
            check_list.append(str(p+1))
            if check_list in total_list:
                count+=bd
                continue
            else:
                count+=rd
                continue
        print("case#"+str(d)+": "+str(count-len(c)))
    else:
        pass

test_case=int(input())
case=0
for t_itr in range(test_case):
    first=input().rstrip().split()
    no_of_cherry=int((first[0]))
    black_strand=int((first[1]))
    pairs=[]
    for j in range(black_strand):
        pairs.append(input())
    result=minimumSugar(no_of_cherry,black_strand,pairs,case)
