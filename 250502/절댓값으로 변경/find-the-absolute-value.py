n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def fun(arr):
    for x in arr:
        print(abs(x),end=" ")
fun(arr)