n = int(input())
#x1, y1, x2, y2 = [], [], [], []
offset = 100 #구간이 [0,200]
checked=[[0] * 200 for _ in range(200)]
cnt=0   #1의 갯수 세기 위해서

for _ in range(n):
    a, b, c, d = map(int, input().split())
    '''
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)
    '''
    #c-1,d-1까지
    for x in range(a,c):
        for y in range(b,d):
            checked[x][y]+=1

for i in range(200):
    for j in range(200):
        if checked[i][j] != 0:
            cnt += 1

print(cnt)





