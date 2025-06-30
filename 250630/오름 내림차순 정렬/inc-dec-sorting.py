n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
for i in range(n):
    print(nums[i],end=" ")
print()

nums.sort(reverse=True)
for i in range(n):
    print(nums[i],end=" ")