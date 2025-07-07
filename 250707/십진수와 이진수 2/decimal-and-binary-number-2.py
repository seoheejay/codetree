N = input() #10011
num = 0
# 10011 >10진수 19 > *17 > 323 > 이진수로 표현
for n in N:
    num = num*2+int(n)

num *=17
lst = []
while(True):
    if num<2:
        lst.append(num)
        break
    lst.append(num%2)
    num//=2
for i in lst[::-1]:
    print(i,end="")
