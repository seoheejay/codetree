n = int(input())
#(5,9),(3,7) 구간으로 받음
lst = [tuple(map(int, input().split()))for _ in range(n)]

#시간 구하기
'''
def total_time(i):
    x1,x2 = lst[i]
    min_x = 0
    max_y = 0
    for j in range(n):
        if j==i:
            continue
        x,y = lst[j]
        min_x = min(min_x,x)
        max_y = max(max_y,y)
    return(max_y-min_x)
'''
def total_time(i):
    cnt=[0]*1001
    
    for j in range(n):
        if j==i:
            continue
        x1,x2 = lst[j]
        for k in range(x1,x2): #끝 포함 안 함
            cnt[k]=1

    return(sum(cnt))
        


max_time = 0
for i in range(n):
    max_time= max(max_time,total_time(i))
print(max_time)