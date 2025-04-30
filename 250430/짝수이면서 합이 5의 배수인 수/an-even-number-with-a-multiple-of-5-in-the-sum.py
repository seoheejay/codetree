n = int(input()) #2자리 숫자

# Please write your code here.
def fun(n):
    #n이 짝수면서, 각 자리 숫자 합이 5의 배수 > yes
    if (n%2==0) and ((n%10+n//10)%5==0):
        print("Yes")
    else:
        print("No")


fun(n)