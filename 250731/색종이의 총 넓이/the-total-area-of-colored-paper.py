n = int(input())
#모든 색종이가 붙여진 이후의 총 넓이 구하기
offset = 100 #구간[0,200] 
checked=[[0]*201 for _ in range(201)]
cnt=0
#가로 세로 8인 정사각형64
for _ in range(n):
    x,y = map(int,input().split())
    #구간 [0,200]
    x+=offset
    y+=offset
    for i in range(x,x+8):
        for j in range(y,y+8):
            checked[i][j]+=1

for i in range(201):
    for j in range(201):
        if checked[i][j]>=1:
            cnt+=1

print(cnt)