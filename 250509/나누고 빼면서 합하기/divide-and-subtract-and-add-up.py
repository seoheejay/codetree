n, m = map(int, input().split())
A = list(map(int, input().split()))
sum = 0
while m>0:
    sum+=A[m-1]
    if m==1:
        break
    elif m%2!=0:
        m-=1
    else:
        m//=2
print(sum)
