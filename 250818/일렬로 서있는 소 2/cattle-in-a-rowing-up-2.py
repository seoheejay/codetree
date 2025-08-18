n = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        #for k in range(i+2, n): 이거 조심하기 j보다 크면 됨
        for k in range(j+1,n):
            if arr[i]<=arr[j]:
                if arr[j]<=arr[k]:
                    cnt+=1
print(cnt)