#상하좌우 특정 방향으로 움직임
#벽에 부딪히면 -> 방향 반대로 움직임 -> 이때 시간 1만큼 소요됨
n,t = map(int,input().split()) #t초
r,c,d = input().split()  #d는 U,D,R,L중 하나
r,c = int(r)-1, int(c)-1 #초기에 구슬 r행 c열에 놓여져 있음을 의미


def range_check(x,y):
    if 0<=x and x<n and 0<=y and y<n : return True
    else: return False

#상하좌우, 끝쪽가면 반대방향으로 -> 0,3 짝 지어주고 1,2 짝 지어주기
dxs, dys = [0,1,-1,0],[1,0,0,-1] #R,D,U,L
mapper={'R':0, 'D':1, 'U':2, 'L':3}
move_dir = mapper[d]

for i in range(t): #t초동안
    nr, nc = r+dxs[move_dir], c+dys[move_dir]
    if range_check(nr, nc):
        r, c = nr, nc
    else:
        move_dir = 3 - move_dir #움직이는 것도 1초로 간주해서 여기서 움직이진 않음

#지금 내가 0based로 했으니깐, 출력은 +1씩 해줘야 함
print(r+1,c+1)