import sys
n = int(input())
arr = list(map(int, input().split()))
#모든 사람의 이동 거리의 합이 최소가 되도록
int_min = sys.maxsize

min_val = int_min

res = 0 
cnt = 1 #첫 번째 집 ~ n 번째 집
for _ in range(n): #n번만큼 반복시키고
    for i in range(n):
        res+=arr[i]*abs(i+1-cnt)
    cnt+=1
    min_val=min(min_val, res)
    res=0
   

print(min_val)