A = input()

# Please write your code here.
def fun(A):
    arr=list(A)
    cnt=0
    x=arr[0] #codetree
    for j in range(1,len(arr)):
        if x!=arr[j]:
            cnt+=1
            
    if cnt>=2:
        print("Yes")
    else:
        print("No")
fun(A)