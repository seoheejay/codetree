n, m = map(int, input().split())
arr = list(map(int, input().split())) #n개의 원소로 이루어짐
queries = [tuple(map(int, input().split())) for _ in range(m)] #m개의 정수쌍

#N개의 원소로 이루어진 수열 A
#M개의 두 정수쌍 a1, a2
#M번에 걸쳐 수열 A의 a1부터 a2까지 합을 구해 출력
#단 수열A 전역변수로 표현

for i in range(m): #4번
    #queries[0]의 a1:1 a2:2 >>> arr[0]+arr[1]
    sum = 0
    a1 = queries[i][0] #1
    a2 = queries[i][1] #2
    for j in range(a1,a2+1):
        sum+=arr[j-1]
    print(sum)
    
