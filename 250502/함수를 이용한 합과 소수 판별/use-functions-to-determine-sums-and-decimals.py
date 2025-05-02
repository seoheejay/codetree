a, b = map(int, input().split())

# Please write your code here.
def fun(a,b):
    cnt=0
    sum=0
    for i in range(a,b+1):
        #소수이면서 모든 자릿수의 합이 짝수인 수의 개수
        sum = i%10 + i//10 
        if i==2:    cnt+=1
        elif i>2:
            if sum%2==0:
                #소수 판별
                for j in range(2,i):
                    if i%j==0:
                        break
                    if j==i-1:
                        cnt+=1
        else:
            continue
    print(cnt)

fun(a,b)
                    