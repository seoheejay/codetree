n, m, k = map(int, input().split()) #n명 학생, m번에 걸쳐서...,k번 이상 벌칙 받게 되면
ans = -1 #m번 지났는데도 벌금 내는 학생 없으면 -1출력
lst = [0]*(n+1)
for i in range(m):
    j = int(input())
    lst[j]+=1
    if lst[j]>=k:
        ans = j
        break
print(ans)


