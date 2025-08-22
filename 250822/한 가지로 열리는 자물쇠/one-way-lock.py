#1~N -> 중복해서 뽑아서 총3자리 자물쇠 만듦
#한 자리라도 주어지는 조합과 거리가 2 이내라면 열리게 됨
n = int(input())
lst = list(map(int, input().split()))
cnt = 0 #조합 수 세기용
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if abs(i-lst[0])<=2 or abs(j-lst[1])<=2 or abs(k-lst[2])<=2:
                cnt+=1
print(cnt)