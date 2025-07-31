offset = 1000 #구간[0,2000]
checked=[[0]*2001 for _ in range(2001)]
cnt=0
for i in range(2):
    x1,y1,x2,y2=map(int,input().split())
    for x in range(x1+offset,x2+offset):
        for y in range(y1+offset,y2+offset):
            if i==0:
                checked[x][y]+=1
            else:
                checked[x][y]-=1 #겹친 게 있으면 0으로 표시되어있을거임
'''
이러면 A-B 넓이로 나옴
for i in range(2001):
    for j in range(2001):
        if checked[i][j] == 1:
            cnt += 1
print(cnt)
'''
# 잔해 영역 감싸는 최소 사각형 구하기
xmin, xmax = 2001, -1
ymin, ymax = 2001, -1

for i in range(2001):
    for j in range(2001):
        if checked[i][j] == 1:
            xmin = min(xmin, i)
            xmax = max(xmax, i)
            ymin = min(ymin, j)
            ymax = max(ymax, j)

if xmin > xmax:
    print(0)
else:
    print((xmax - xmin + 1) * (ymax - ymin + 1))