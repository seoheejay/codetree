n = int(input())
x,y=0,0
#(1,0),(-1,0),(0,-1),(0,1) 동E서W남S북N
dx, dy = [1,-1,0,0],[0,0,-1,1]
for _ in range(n):
    d,t=input().split()
    for _ in range(int(t)):
        if d=="E":
            x,y = x+dx[0], y+dy[0]
        elif d=="W":
            x,y = x+dx[1], y+dy[1]
        elif d=="S":
            x,y = x+dx[2], y+dy[2]
        elif d=="N":
            x,y = x+dx[3], y+dy[3]
print(x,y)