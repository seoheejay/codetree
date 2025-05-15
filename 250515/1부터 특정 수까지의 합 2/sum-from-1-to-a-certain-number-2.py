N = int(input())

# Please write your code here.
def fun(N):
    if N==0:
        return 0
    return N+fun(N-1)

print(fun(N))