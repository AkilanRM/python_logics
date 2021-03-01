n=int(input("enter the no. of friends:"))
skill_list=[]
ans=[]
minimum_skill=int((input("enter the minimum skill:")))
for i in range(0,n):
    skill_list+=[int(input())]

print(skill_list)
for j in range(len(skill_list)):
    if(skill_list[j] >= minimum_skill):
        ans+=["yes"]
    else:
        ans+=["no"]
for x in ans:
    print(x)
