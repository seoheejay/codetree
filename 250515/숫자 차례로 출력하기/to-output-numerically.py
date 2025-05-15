n = int(input())

# Please write your code here.
def fun1(n):
    for i in range(1,n+1):
        print(i,end=" ")
    print()
    fun2(n)
def fun2(n):
    for i in range(n,0,-1):
        print(i, end=" ")

fun1(n)