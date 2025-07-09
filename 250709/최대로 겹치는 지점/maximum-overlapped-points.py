n = int(input())
#segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
cnt=[0]*101
for _ in range(n):
    a,b = map(int,input().split())
    for i in range(a,b+1): #끝점에서 닿는 경우도 겹치는 걸로 봄 따라서 b+1
        cnt[i]+=1

print(max(cnt))