x,y = map(int, input().split())

#x이상 y이하 수 중 각 자리 숫자의 합이 최대
maxsum = 0
for i in range(x,y+1):
    s=0
    while(i>=10):
        #if i=35
        s+=i%10 #s+=5
        i//=10 #35 -> 3
    s+=i
    maxsum=max(maxsum,s)

print(maxsum)