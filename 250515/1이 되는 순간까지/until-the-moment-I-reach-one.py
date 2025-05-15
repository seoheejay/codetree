N = int(input())

# Please write your code here.
cnt=0
def f(N,cnt):
    if N==1:
        return cnt
    if N%2==0:
        cnt+=1
        return f(N//2,cnt)
    else:
        cnt+=1
        return f(N//3,cnt)
print(f(N,cnt))