#개발자 6 -> 3명/3명으로 배정
#능력간 총합간의 차이 최소화하기

lst = list(map(int, input().split()))

def chek_diff(i,j,k):
    sum1 = lst[i]+lst[j]+lst[k]
    sum2 = sum(lst) - sum1
    return abs(sum1-sum2)

min_diff = 1000000
for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            min_diff = min(min_diff, chek_diff(i,j,k))

print(min_diff)
