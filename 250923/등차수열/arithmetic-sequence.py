#N개의 수, 자연수K 적절히 정의하여 (ai,K,aj)가 등차수열 이루는 최대 횟수 정하기
#1<=i<=j<=N
#등차수열 이룬다는 말은 (aj-K) == (K-ai)

N = int(input())
lst = list(map(int, input().split())) #[7,6,4,3]

#근데 이제 K의 범위가 안 나와있는데 가장 큰 수 보다 클 순 없음!
cnt, max_cnt= 0,0
for K in range(1,max(lst)+1):
    cnt = 0
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            # abs 쓰면 안됨 if abs(lst[i]-K) == abs(lst[j]-K):
            if (lst[j]-K) == (K-lst[i]):
                cnt+=1
    max_cnt = max(max_cnt,cnt)

print(max_cnt)




