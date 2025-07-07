n, k = map(int, input().split())

#n개의 칸이 있음
#명령이 K번 주어짐
#1부터 n번 칸까지 쌓인 블럭의 수 중 최댓값 출력 > 누적값 
lst =[0]*n 

for _ in range(k):
    a,b = map(int,input().split())
    for j in range(a,b+1):
        lst[j-1]+=1
print(max(lst))