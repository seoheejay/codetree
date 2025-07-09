n = int(input())
# Please write your code here. 
#구간과 지점은 다름
cnt = [0]*201
#n개의 선분
lst = []
for _ in range(n):
    a,b = map(int, input().split()) # (1,5)
    for i in range(a, b+1):
        cnt[i]+=1
"""
인덱스 구하는 줄 알았음
max_idx = 0

for i in range(len(cnt)):
    if max_idx < cnt[i]:
        max_idx = i
print(max_idx)

"""
print(max(cnt))