n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
maxnum = 0
def fun(arr,n, maxnum):
    if n == 0: 
        return maxnum
    return fun(arr,n-1,max(maxnum, arr[n-1]))
    
print(fun(arr,n,maxnum))
