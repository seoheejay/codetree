n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
reslist=[]
for x in str: #apple, appreciate...
    res = True
    for i in range(len(t)):
        if (x[i]!=t[i]):
            res = False
            break
    if res==True:
        reslist.append(x)

reslist.sort()
#reslist=sorted(reslist)
#print(reslist)
print(reslist[k-1])
