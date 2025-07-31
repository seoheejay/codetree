#구간 찾는 거니깐 x1, x2-1까지
#음수좌표 > offset = 1,000 주어지는 x값의 최소가 -1000이므로 > 즉 구간은 [0,2000] 내에서 
offset = 1000
max_r = 2000

n = int(input())
segements = []

#현재위치
cur = 0

for _ in range(n):
    distance, direction = tuple(input().split())
    distance = int(distance)

    if direction=='L':
        #왼쪽으로 이동할 경우 cur - distance 부터 cur까지
        section_l = cur - distance
        section_r = cur
        cur -= distance
    else:
        section_l = cur 
        section_r = cur+distance
        cur+=distance

    segements.append([section_l,section_r])

checked = [0]*(max_r+1)

for x1, x2 in segements:
    #offset더해주기
    x1,x2 = x1+offset, x2+offset
    #구간이므로 x2+1말고 x2
    for i in range(x1,x2):
        checked[i]+=1

cnt=0
#2번이상지나간영역의 크기
for elem in checked:
    if elem>=2:
        cnt+=1

print(cnt)
