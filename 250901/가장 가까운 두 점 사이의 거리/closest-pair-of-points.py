import sys
INT_MAX = sys.maxsize

n = int(input())
points =  [tuple(map(int, input().split())) for _ in range(n)]

# 두 점 사이의 거리의 제곱 값 반환
def dist(i,j):
    x1,y1 = points[i]
    x2,y2 = points[j]
    return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

#최솟값 찾기
min_dist = INT_MAX
for i in range(n):
    for j in range(i+1,n):
        min_dist = min(min_dist, dist(i,j))

print(min_dist)