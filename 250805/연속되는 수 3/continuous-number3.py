n = int(input()) #0은 주어지지 않는다고 가정
#부호가 동일한 정수로만 이루어진 부분 수열 중 최대 길이 구하기
arr = [int(input()) for _ in range(n)] #[2,-1,-5,-2,-3,5,8]
lst = [0]*(n+1) #음수, 양수 기록용 리스트
for i in range(n):
    if arr[i] < 0:
        lst[i] = 1 #음수
    else:
        lst[i] = 2
    #[2,1,1,1,1,2,2]
cnt = [0]*(n+1) #[0,1,2,3,0,1]
for i in range(1,n): #1,2,3,4,n-1
    if lst[i-1]==lst[i]:
        cnt[i]=cnt[i-1]+1
    else:
        cnt[i]=0
print(max(cnt)+1)



