def diagonalDifference(arr):
    val=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if(i==j):
                val+=arr[i][j]
    print(val)




n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
