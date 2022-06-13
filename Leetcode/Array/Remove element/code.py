nums = [3,2,2,3,7,9,8,6]
val = 2

j = 0
for i in nums:
    if i != val:
        nums[j] = i
        j += 1


print(nums)