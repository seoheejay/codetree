text = input()
pattern = input()

# Please write your code here.
num = -1
for i in range(len(text)-len(pattern)+1):
    if text[i:i+len(pattern)] == pattern:
        num = i
        print(num)
        break
else:
    print(num)
        
