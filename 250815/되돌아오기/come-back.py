n = int(input())

#동E 남S 서W 북N
dxs, dys = [0,1,0,-1],[1,0,-1,0]
x, y = 0,0
cnt = 0 
res = False

for _ in range(n):
    if res:
        break
    d,t = input().split()
    for i in range(int(t)):
        if d=="E":
            x, y = x + dxs[0] , y+dys[0]
        elif d=="S":
            x, y = x + dxs[1], y+dys[1]
        elif d=="W":
            x, y = x + dxs[2] , y+dys[2]
        elif d=="N":
            x, y = x + dxs[3] , y+dys[3]
        cnt+=1
        if x==0 and y==0:
            res = True
            break

if res:
    print(cnt)
else:
    print("-1")

