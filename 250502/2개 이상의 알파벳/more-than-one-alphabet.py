A = input()

# Please write your code here.
def fun(A):
    arr=set(A)           
    if len(arr)>=2:
        print("Yes")
    else:
        print("No")
fun(A)