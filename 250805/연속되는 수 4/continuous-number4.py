n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt, maxcnt= 0,0
for i in range(1,n): #[1,5,2,3,5,8,8]
    if arr[i-1]<arr[i]:
        cnt+=1
    else:
        maxcnt = max(cnt,maxcnt)
        cnt=0

maxcnt = max(cnt, maxcnt) #만약 마지막이 증가로 끝났을 경우 고려
print(maxcnt+1)