n = int(input())
# Please write your code here. 
#구간과 지점은 다름
cnt = [0]*201

#음수처리 추가
shift = 100

#n개의 선분
lst = []
for _ in range(n):
    a,b = map(int, input().split()) # (1,5)
    for i in range(a, b): #끝점 포함X 추가
        cnt[i+shift]+=1
"""
인덱스 구하는 줄 알았음
max_idx = 0

for i in range(len(cnt)):
    if max_idx < cnt[i]:
        max_idx = i
print(max_idx)

"""
print(max(cnt))