n = int(input())
cnt = 0
#입력x1,x2받는데 -> 해당 선분의 끝점이 (x1,0) (x2,1)을 의미함
#not(x1,x2)
x = [tuple(map(int, input().split()))for _ in range(n)]

#다른 선분과 겹치지 않는 선분의 수 구하기
for i in range(n):
    #i번째 선분이 다른 선분과 겹치지 않는지 확인
    overlap = False

    for j in range(n):
        #자기 자신 제외
        if i == j:
            continue
        #선분이 겹치는 경우 2가지가 있음
        if (x[i][0] <= x[j][0] and x[i][1]>=x[j][1]) or (x[i][0]>=x[j][0]and x[i][1]<=x[j][1]):
            overlap = True
            break
    #겹치지 않았다면 정답 개수에 하나 추가하기
    if overlap == False:
        cnt+=1


print(cnt)