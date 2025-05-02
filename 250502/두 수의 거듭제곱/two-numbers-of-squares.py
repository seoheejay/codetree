a, b = map(int, input().split())

# Please write your code here.
def fun(a,b):
    sum=1
    for _ in range(b):
        sum*=a
    print(sum)
fun(a,b)