n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
#arr.sort() 얘를 미리 하면 안됐음
res=[]
#홀수 번째 원소가 주어질 때마다 지금까지 입력받은 값의 중앙값 출력
for i in range(1,n+1):
    res.append(arr[i-1])
    if i%2!=0: #홀수면 중앙값 출력 1이면 > 1, 3이면 > 2, 5이면 > 3
        res.sort()
        print(res[((1+i)//2)-1],end=" ")
    else:
        continue
