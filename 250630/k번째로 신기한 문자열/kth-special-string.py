n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.

for x in str: #apple, appreciate...
    if (x[0]!=t[0])or(x[1]!=t[1]):
        str.remove(x)

str.sort()
print(str[k])
