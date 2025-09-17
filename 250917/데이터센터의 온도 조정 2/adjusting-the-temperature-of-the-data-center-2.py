n, c, g, h = map(int, input().split())

# 장비 온도 구간 저장
ab = []
for i in range(n):
    a, b = map(int, input().split())
    ab.append((a, b))

# 특정 온도에서의 작업량 (한 장비 기준)
def output(a, b, t):
    if t < a:
        return c
    elif t <= b:   
        return g
    else:
        return h

# 특정 온도에서 모든 장비 작업량 합산
def performance(t):
    total = 0
    for a, b in ab:
        total += output(a, b, t)
    return total

# 최댓값 구하기
max_output = 0
for t in range(1001): 
    max_output = max(max_output, performance(t))

print(max_output)
