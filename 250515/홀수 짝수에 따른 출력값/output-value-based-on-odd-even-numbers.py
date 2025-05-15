N = int(input())

# Please write your code here.
def f(N):
    if N==1 or N==2:
        return N

    return f(N-2)+N
print(f(N))
