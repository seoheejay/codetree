n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def fun(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i]//=2
    return arr
fun(arr)

for i in range(n):
    print(arr[i],end=" ")
