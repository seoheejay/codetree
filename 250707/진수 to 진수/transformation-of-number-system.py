a, b = map(int,input().split())
n = input()

lst=[]
#A진수 N을 > 10진수로 변환 후에 > B진수로
num=0
for i in n:
    num=num*a+int(i)

while(True):
    if num<b:
        lst.append(num)
        break
    lst.append(num%b)
    num//=b

for j in lst[::-1]:
    print(j,end="")