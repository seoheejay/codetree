a,b,c = map(int, input().split())

#분으로 다 바꾸자
start = 11*24*60 + 11*60 + 11
end = a*24*60 + b*60 + c

if end < start:
    print(-1)
else:
    print(end - start)

"""
이건 시간초과 나왔음
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
"""