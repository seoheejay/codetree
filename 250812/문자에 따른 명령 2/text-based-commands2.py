x,y = 0,0 
#현재 북쪽을 향한 상태
#d="N" 문자 말고 index로 사용하자
d = 3
#L > 왼쪽으로 90도 방향전환
#R > 오른쪽으로 90도 방향전환
#F > 바라보고 있는 방향으로 +1
dx, dy = [1,0,-1,0],[0,-1,0,1] #동E>0,남S>1,서W>2,북N>3
lst = list(input()) #LF
for i in range(len(lst)):
    if lst[i]=="L":
        d = (d+3)%4
    elif lst[i]=="R":
        d = (d+1)%4
    else:
        x, y = x+dx[d], y+dy[d]


print(x,y)