n, m = map(int, input().split())

# a와 b의 매 시간별 누적 거리 기록
a_dist = []
b_dist = []

# a
dist = 0
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):  # 매 시간 단위로 누적
        dist += v
        a_dist.append(dist)

# b
dist = 0
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        dist += v
        b_dist.append(dist)

# 선두 변화 횟수 계산
cnt = 0
leader = None  # 현재 선두
for i in range(len(a_dist)):
    if a_dist[i] > b_dist[i]:
        now = "a"
    elif a_dist[i] < b_dist[i]:
        now = "b"
    else:
        now = leader  # 같으면 이전 선두 유지

    if leader and now != leader:  # 선두가 바뀐 경우
        cnt += 1
    leader = now

print(cnt)

'''
처음에
거리 누적 방식 오류
a_lst[i+1] = a_lst[i] + (v * t) 로 했었는데,
이렇게 하면 "각 구간의 끝"에만 값이 기록되고,
나머지 시간 동안의 거리 변화가 반영되지 않음.
'''