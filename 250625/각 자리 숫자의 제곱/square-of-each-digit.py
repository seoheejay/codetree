N  = int(input())

def fun(N):
    if N<10:
        return N*N
    return fun(N//10)+(N%10)*(N%10)

print(fun(N))

