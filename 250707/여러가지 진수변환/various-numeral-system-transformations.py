N, B = map(int, input().split())

# Please write your code here.
#B는 4or8
#N은 10진수

lst = []
while(True):
    if N<B:
        lst.append(N)
        break
    lst.append(N%B)
    N//=B

for i in lst[::-1]:
    print(i,end="")