n, m = map(int, input().split())
#A가 움직이는 횟수 M, B가 움직이는 횟수 M

#어느 방향으로 얼만큼 움직였는지가 주어짐
# A와 B가 바로 직전에는 다른 위치에 있다가 -> 그 다음 번에 같은 위치에 오게 되는 경우가 총 몇 번?
cnt = 0
#단, 처음엔 같은 위치에 있는데 이건 포함하지 않음

# t초만큼 d방향으로 이동함
pos_a,pos_b = [0]*50001, [0]*50001

# a
time_a=1
for _ in range(n):
    time, direction = input().split()
    for _ in range(int(time)):
        pos_a[time_a] = pos_a[time_a-1] + (1 if direction == "R" else -1)
        time_a+=1

# b
time_b = 1
for _ in range(m):
    time, direction = input().split()
    for _ in range(int(time)):
        pos_b[time_b] = pos_b[time_b-1] + (1 if direction == "R" else -1)
        time_b+=1

max_t = max(time_a,time_b)
for i in range(1,max_t+1): #index 0은 cnt에 포함하지 않음
    #직전에 다른 위치에 있다가 다음 번에 같은 위치에 오게 되는 경우
    #if i!=1 and (pos_a[i-1]!=pos_b[i-1]) and (pos_a[i]==pos_b[i]):
    if i==1 and (pos_a[i]==pos_b[i]):
        cnt+=1
    elif i!=1 and (pos_a[i-1]!=pos_b[i-1]) and (pos_a[i]==pos_b[i]):
        cnt+=1
print(cnt)


