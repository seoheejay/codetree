A =[]
B =[]
M =[]
check =[[0]*2000 for _ in range(2000)] #넓이 적기
cnt=0 #넓이 세기
for i in range(3):
    x1,y1,x2,y2 = map(int,input().split()) #좌측 최하단 좌표, 우측 최상단 좌표
    for x in range(x1,x2):
        for y in range(y1,y2):
            if i!=2:
                check[x][y]+=1
            else:
                check[x][y]-=1 #M은 빼주려고
#A,B 겹치지 않게 주어진다고 가정했으니
for x in range(2000):
    for y in range(2000):
        if check[x][y]==1:
            cnt+=1

print(cnt)