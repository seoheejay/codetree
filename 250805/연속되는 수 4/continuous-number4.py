n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt, maxcnt= 0,0
for i in range(n):
    if arr[i-1]<arr[i]:
        cnt+=1
    else:
        maxcnt = max(cnt,maxcnt)
        cnt=0
print(maxcnt+1)