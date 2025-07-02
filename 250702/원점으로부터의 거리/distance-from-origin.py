n = int(input()) #점의 수
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]
#(x,y) #원점과 가까운 점부터 순서대로 번호를 출력
# Please write your code here.



points.sort(key=lambda x: abs(x[1][0]+x[1][1]))

for point in points:
    print(point[0]+1)