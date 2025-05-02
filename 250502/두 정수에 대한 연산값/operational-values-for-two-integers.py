a, b = map(int, input().split())

# Please write your code here.
#둘 중 큰 수에 +25
#작은 수에 *2

def fun(a,b):
    big = max(a,b)
    if big==a:
        a+=25
        b*=2
    else:
        a*=2
        b+=25
    return(a,b)

a,b = fun(a,b)
print(a,b)