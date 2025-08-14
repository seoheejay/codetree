n, m = map(int, input().split())
#n이 행 #m이 열
arr = [[0]*m for _ in range(n)]
x,y = 0,0 #현재위치
#오 y증가, 아 x감소 , 왼 y감소, 위 x증가
dxs, dys = [0,1,0,-1],[1,0,-1,0]
dir_num = 0 

#범위 안에 있는지 체크
def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

value = 0

for i in range(n):
    for j in range(m):
        value +=1
        arr[x][y]=value
        nx, ny = x+dxs[dir_num], y+dys[dir_num]
        if not in_range(nx,ny) or arr[nx][ny] !=0 : #비어져있어야 하니깐
            dir_num = (dir_num+1)%4
            #이렇게 한 다음 index에다가 값 넣기
            nx, ny = x+dxs[dir_num], y+dys[dir_num]
        x, y = nx, ny

#출력
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()
