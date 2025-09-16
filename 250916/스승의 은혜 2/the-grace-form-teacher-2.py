#n명의 학생에게 b만큼의 예산 
n, b = map(int, input().split())

#학생이 원하는 가격 P(i)
#선생님에게는 선물 한 개 정해서 -> 반값 할인받을 수 있는 쿠폰 있음(1개)
lst = [int(input()) for _ in range(n)] #[4, 2, 8, 6, 12]
#coupon = False

#선생님이 선물 가능한 학생의 최대 명수
maxcnt = 0

#최대 명수니깐 -> sort 정렬이용하자 [2,4,6,8,12]
lst.sort()
''' 아래와 같이 짜면, 최적의 해가 아님
for i in range(n):
    if b<lst[i]:
        if coupon == True: #이미 쿠폰 썼으니깐
            break
        else:
            if b <= (lst[i]//2):
                b-=(lst[i]//2)
                maxcnt+=1
                coupon=True
            continue #이거 안해주면 밑에거 실행됨
    
    b-=lst[i] #예산에서 빼기 (선물 가격 항상 짝수 조건있음)
    maxcnt+=1
'''
# i번째 학생에게 쿠폰 쓴다고 가정
for i in range(n):
    budget = b
    cnt = 0
    for j in range(n):
        price = lst[j]
        if j == i:  # i번째 학생은 쿠폰 적용
            price //= 2
        if budget >= price:
            budget -= price
            cnt += 1
        else: 
            break
    maxcnt = max(maxcnt, cnt)

    

print(maxcnt)