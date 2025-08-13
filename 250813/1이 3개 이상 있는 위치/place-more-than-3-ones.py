n = int(input())
lst = []
dxs, dys = [0,1,0,-1],[1,0,-1,0] #격자 아니고 행열

for _ in range(n):
    row = list(map(int, input().split()))
    lst.append(row)

def check_range(x,y):
    if 0<=x and x<n and 0<=y and y<n:
        return True
    else: return False

x, y = 0,0
cnt = 0
res = 0
for i in range(n):
    for j in range(n):
        cnt=0
        for dx,dy in zip(dxs,dys):
            x,y = i+dx, j+dy
            if check_range(x,y) and lst[x][y]==1:
                cnt+=1
        if cnt>=3: res+=1

print(res)