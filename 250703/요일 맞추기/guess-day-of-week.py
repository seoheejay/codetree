m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
#        1, 2,3, 4, 5, 6, 7,  8, 9 ,10,11,12
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#m1,d1  월요일이었음
#m2,d2 는 무슨 요일?

#while로 구현했다가 시간초과 떴었음

# m월 d일 → 1월 1일부터 며칠째인지 계산
def total_days(m, d):
    return sum(days[1:m]) + d

# 기준일과 목표일의 차이
diff = total_days(m2, d2) - total_days(m1, d1)

# 요일 계산 
# 음수일 때 -1%7 = 6나옴 0 이상 7미만
# -2%7 = 5 나옴
print(day[(diff%7)])