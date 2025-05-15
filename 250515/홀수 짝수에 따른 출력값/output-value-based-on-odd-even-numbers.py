N = int(input())

# Please write your code here.
def f(N):
    if N==1:
        return N
    if N==2:
        return N
    if N%2==0:
        return f(N-2)+N
    else:
        return f(N-2)+N
print(f(N))
