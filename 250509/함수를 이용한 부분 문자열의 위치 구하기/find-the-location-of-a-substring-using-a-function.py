text = input()
pattern = input()

# Please write your code here.
for i in range(len(text)-1):
    result = False
    num = 0
    for j in range(len(pattern)-1):
        if text[i] == pattern[j]:
            result = True
            num = i
        else:
            result = False
if result==True:
    print(num)
else:
    print("-1")
