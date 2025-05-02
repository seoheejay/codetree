a, b = map(int, input().split())

# Please write your code here.
def fun(a,b):
    minA = min(a,b)
    if minA==a:
        a+=10
        b*=2
    else:
        a*=2
        b+=10
    return(a,b)


a,b =fun(a,b)
print(a,b)