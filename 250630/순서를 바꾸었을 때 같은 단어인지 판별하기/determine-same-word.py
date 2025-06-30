word1 = input()
word2 = input()

# Please write your code here.
word1 = sorted(word1)
word2 = sorted(word2)

res=True

if len(word1) != len(word2):
    res=False
else:
    for i in range(len(word1)):
        if word1[i]!=word2[i]:
            res=False
            break

if res==True:
    print("Yes")
else:
    print("No")