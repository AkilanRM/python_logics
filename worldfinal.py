def acmTeam(topic):
    maxtopics=[]
    for x in range(0,len(topic)):
        if(x==len(topic)-1):
            break
        for i in range(x+1,len(topic)):
            maxi=0
            if(i==x):
                continue
            for j,k in zip(topic[x],topic[i]):
                
                if(j==k):
                    if(j=='1'):
                        maxi+=1
                    else:
                        continue
                else:
                    maxi+=1
            maxtopics+=[maxi]
    print(maxtopics)
    topics=max(maxtopics)
    pairs=maxtopics.count(topics)
    print("TOPICS_KNOWN:"+str(topics))
    print("PAIRS_OF_ATTENDEES:"+str(pairs))

nm = input().split()

n = int(nm[0])
m = int(nm[1])

topic = []

for _ in range(n):
    topic_item = input()
    topic.append(topic_item)

result = acmTeam(topic)

    
