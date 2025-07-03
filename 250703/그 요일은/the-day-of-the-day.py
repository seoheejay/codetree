m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
#        1, 2,3, 4, 5, 6, 7,  8, 9 ,10,11,12
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

#m1,d1 월요일,, m2,d2까지 A요일 몇 전 등장?
#앞선요일 없음

def total_days(m,d):
    return sum(days[1:m])+d

diff = total_days(m1,d1)-total_days(m2,d2)

def dayc(diff,day):
    cnt = 0 #d1은 월요일, A요일 몇 번 등장하는지?
    cnt = diff//7 
    # 나머지 사용해서 한 번 더 나오는지 안 나오는지 여부 따져줘야 함
    for i in range(diff%7):
        if A==day[i]:
            cnt+=1
    print(abs(cnt))

dayc(diff,day)

