a, b = map(int, input().split())

# Please write your code here.
def fun(a,b):
    sum=0
    for i in range(a,b+1):
        for j in range(2,i):
            if i%j==0:
                break
            if j==i-1:
                sum+=i
    print(sum)


fun(a,b)