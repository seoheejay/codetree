a, b, c = map(int, input().split())

# Please write your code here.
cnt = 0
day = 11
hour = 11
minu = 11

while(True):
    if day == a and hour == b and minu == c:
        break
    
    minu+=1
    cnt+=1
    if minu==60:
        minu=0
        hour+=1
    if hour==24:
        hour=0
        day+=1
print(cnt)