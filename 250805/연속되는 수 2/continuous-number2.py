n = int(input())
cnt=0
num=0
lst = []
for i in range(n):
    num = int(input())
    lst.append(num)
for i in range(n):
    if i==0 or lst[i-1]!=lst[i]:
        cnt+=1
print(cnt)
