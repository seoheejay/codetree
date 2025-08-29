import sys

INT_MAX = sys.maxsize

#변수 선언 및 입력
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

ans = INT_MAX #이건 넓이 최솟값 담을 변수

#빼야하는 점의 위치 정하기 : i번째 점을 빼자
#직사각형 넓이 구하려면 x,y좌표 각각 최대-최소
for i in range(n):
    min_x, max_x = INT_MAX, 1
    min_y, max_y = INT_MAX, 1
    for j,(x,y) in enumerate(points):
        #i번째 점은 제외할거니깐
        if j==i:
            continue
        min_x = min(min_x,x)
        max_x = max(max_x,x)
        min_y = min(min_y,y)
        max_y = max(max_y,y)

    ans = min(ans,(max_x-min_x)*(max_y-min_y))

print(ans)