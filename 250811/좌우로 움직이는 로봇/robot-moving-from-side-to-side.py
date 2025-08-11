n, m = map(int, input().split())
#A가 움직이는 횟수 N, B가 움직이는 횟수 M

#어느 방향으로 얼만큼 움직였는지가 주어짐
# A와 B가 바로 직전에는 다른 위치에 있다가 -> 그 다음 번에 같은 위치에 오게 되는 경우가 총 몇 번?
cnt = 0
#단, 처음엔 같은 위치에 있는데 이건 포함하지 않음

# t초만큼 d방향으로 이동함
pos_a,pos_b = [0],[0]

# a
# time_a=1
for _ in range(n):
    time, direction = input().split()
    for _ in range(int(time)):
        #원래 크기 미리 지정해줬었는데 지정 빼서 append로 바꿈
        #pos_a[time_a] = pos_a[time_a-1] + (1 if direction == "R" else -1)
        pos_a.append(pos_a[-1]+(1 if direction == "R" else -1))
        #time_a+=1

# b
#time_b = 1
for _ in range(m):
    time, direction = input().split()
    for _ in range(int(time)):
        #pos_b[time_b] = pos_b[time_b-1] + (1 if direction == "R" else -1)
        pos_b.append(pos_b[-1]+(1 if direction == "R" else -1))
        #time_b+=1

#max_t = max(time_a,time_b)
max_t = max(len(pos_a), len(pos_b))

'''
- 상대가 움직임이 끝나고 나서 남는 시간 처리 문제
A와 B가 각각 움직인 시간이 다르면, 짧게 움직인 쪽의 위치가 이후에도 계속 동일하게 유지돼야 비교가 정확합니다.

현재 코드는 움직임이 끝난 뒤 그 이후 시간대의 위치를 기록하지 않아 배열에 0 또는 이전 위치가 반영되지 않아 잘못 비교될 수 있습니다.

'''
#움직임 끝난 후 위치 유지
while len(pos_a) < max_t:
    pos_a.append(pos_a[-1])
while len(pos_b) < max_t:
    pos_b.append(pos_b[-1])

for i in range(1,max_t): #index 0은 cnt에 포함하지 않음
    #직전에 다른 위치에 있다가 다음 번에 같은 위치에 오게 되는 경우
    if (pos_a[i-1]!=pos_b[i-1]) and (pos_a[i]==pos_b[i]):
        cnt+=1
print(cnt)


