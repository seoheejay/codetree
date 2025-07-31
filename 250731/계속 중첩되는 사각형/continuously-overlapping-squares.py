n = int(input())
#처음은 빨간색, 두 번째는 파란색 직사각형
checked=[[0]*201 for _ in range(201)]
offset=100 #구간 0부터 200까지

for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    #0,2,4 ... > 빨간색1
    for x in range(x1+offset,x2+offset):
        for y in range(y1+offset,y2+offset):
            if i%2==0:
                #겹치는 위치엔 가장 마지막에 덮힌 색으로 
                checked[x][y]=1 #그냥 대입시키기
            else:
                checked[x][y]=2 #파란색
cnt=0
#파란색 넓이 구하기 > 따라서 빨간색 1로표시, 파란색2로표시
for x in range(201):
    for y in range(201):
        if checked[x][y]==2:
            cnt+=1
print(cnt)