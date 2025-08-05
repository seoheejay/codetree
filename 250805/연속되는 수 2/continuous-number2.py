n = int(input())
lst = [int(input()) for _ in range(n)]

cnt = 1
max_cnt = 1

for i in range(1, n):
    if lst[i] == lst[i-1]:  
        cnt += 1
        max_cnt = max(max_cnt, cnt)  
    else:
        cnt = 1              

print(max_cnt)
