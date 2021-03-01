def organizingContainers(container):
    x=len(container)
    cont0=[]
    cont1=[]
    for i in range(x):
        if(i==x-1):
            break
        cont0.append(container[0])
        cont1.append(container[1])
    
        if(cont_0==cont_1):
           val="possible"
        else:
            val=""
    if(val=='possible'):
        print("possible")
    
    i









q = int(input())

for q_itr in range(q):
    n = int(input())

    container = []

    for _ in range(n):
        container.append(list(map(int, input().rstrip().split())))

    result = organizingContainers(container)
