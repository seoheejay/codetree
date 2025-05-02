n1, n2 = map(int, input().split()) #n1개의 원소로 이루어져 있는 수열A, n2개의 원소로 이루어져 있는 수열B
a = list(map(int, input().split())) #[1,7,2,8]
b = list(map(int, input().split())) #[7,2]

#수열B가 수열A의 연속부분수열인지를 판단하는 프로그램
#연속부분수열이란? 수열B가 수열A의 원소들을 연속하게 뽑았을 때 나올 수 있는 수열
#ex. 수열A가 [1,7,2,8]일 때, 수열B가 [7,2]라면 O
#ex. 수열B가 [7,8]이면 아님

def fun(a, b, n1, n2):
    for i in range(n1 - n2 + 1):  # 연속 부분 수열 검사
        if a[i:i + n2] == b:
            print("Yes")
            return
    print("No")
              

fun(a,b,n1,n2)