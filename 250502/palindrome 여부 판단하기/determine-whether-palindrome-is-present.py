A = input()

# Please write your code here.
def fun(A):
    res=False
    arr=[]
    arra=list(A) 
    for i in range(len(A)-1,-1,-1): #codetree
        arr.append(A[i])
    if arr==arra:
        res=True
    if res==True:
        print("Yes")
    else:
        print("No")
fun(A)

