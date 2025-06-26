import math

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

def lcm(a, b):
    return a * b // math.gcd(a, b)

def f(arr, n):
    if n == 1:
        return arr[0]
    return lcm(arr[n-1], f(arr, n-1))

print(f(arr, n))
