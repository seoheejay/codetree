N = int(input())

# Please write your code here.
def f(N):
    if N<10:
        return N*N
    return f(N//10)+(N%10)*(N%10)
print(f(N))