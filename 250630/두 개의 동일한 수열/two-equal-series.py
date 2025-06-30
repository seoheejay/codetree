n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()

result=False
for i in range(n):
    if A[i]!=B[i]:
        result=False
        break
    else:
        result=True
if result == True:
    print("Yes")
else:
    print("No")
    