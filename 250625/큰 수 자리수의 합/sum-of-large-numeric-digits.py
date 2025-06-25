a, b, c = map(int, input().split())
N=a*b*c
# Please write your code here.
def fun(N):
    if N<10:
        return N
    return N%10 + fun(N//10)
print(fun(N))
  