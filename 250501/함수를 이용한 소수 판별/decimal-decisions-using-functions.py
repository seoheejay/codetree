a, b = map(int, input().split())

# Please write your code here.
def fun(a, b):
    sum = 0
    for i in range(a, b + 1):
        if i == 1:
            continue  # 1은 소수가 아님
        elif i == 2:
            sum += 2  # 2는 소수
        else:
            is_prime = True  #초기화
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                sum += i
    print(sum)



fun(a,b)