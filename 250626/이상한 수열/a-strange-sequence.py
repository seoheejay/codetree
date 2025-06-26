N = int(input())

# Please write your code here.
def fun(N):
    if N==1:
        return 1
    elif N==2:
        return 2
    return fun(N-1)+fun(N//3)
print(fun(N))