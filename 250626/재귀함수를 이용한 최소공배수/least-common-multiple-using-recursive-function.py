n = int(input())
arr = list(map(int, input().split()))
arr.sort() #1,2,5,6,7,9
lcm = arr[n-1] #이게 가장 큰 수

# Please write your code here.
def f(arr,n,lcm):
    if n==0:
        return lcm
    elif arr[n-1]%arr[n-2] == 0:
        return f(arr,n-1,lcm)
    else:
        for i in range(1,arr[n-2]+1): #작은 수
            if arr[n-2]%i==0:
                if lcm%i==0:
                    continue
                else:
                    lcm*=i 
        return f(arr,n-1,lcm)

        

print(f(arr,n,lcm))
