n = int(input())

# Please write your code here.
def fun(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return(sum//10) 
print(fun(n))