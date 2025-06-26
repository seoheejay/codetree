n = int(input())
cnt = 0
# Please write your code here.
def fun(n,cnt):
    if n==1:
        return cnt
    if n%2==0:
        cnt+=1
        return fun(n//2,cnt)
    else:
        cnt+=1
        return fun(n*3+1,cnt)

print(fun(n,cnt))