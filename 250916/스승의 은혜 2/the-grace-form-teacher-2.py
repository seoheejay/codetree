#n명의 학생에게 b만큼의 예산 
n, b = map(int, input().split())

#학생이 원하는 가격 P(i)
#선생님에게는 선물 한 개 정해서 -> 반값 할인받을 수 있는 쿠폰 있음(1개)
lst = [int(input()) for _ in range(n)] #[4, 2, 8, 6, 12]
coupon = False

#선생님이 선물 가능한 학생의 최대 명수
maxcnt = 0

#최대 명수니깐 -> sort 정렬이용하자 [2,4,6,8,12]
lst.sort()
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
    

print(maxcnt)