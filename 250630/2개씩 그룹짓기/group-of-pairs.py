n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
#2개의 원소가 하나의 그룹을 이루도록!
#그러면 
#만약 1 2 3 5 7 8 이면 최소 최댓값 1,8 > 9
# 2 3 5 5 면 최소 최댓값 3,5 > 8
nums.sort()
#print(nums)
sum = list()

for i in range(n):
    sum.append(nums[i]+nums[2*n-i-1])

sum.sort()
#print(sum)
print(sum[n-1])

