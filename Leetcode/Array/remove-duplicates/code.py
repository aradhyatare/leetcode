nums = [1,1,2]
length = len(nums)
k = 0

# nums[:] = (value for value in nums if nums.count(value) == 2)
print(nums)


nums[:] = list(dict.fromkeys(nums))
print(nums)

# for num in nums:
#     if nums.count(num) > 1: 
#         nums[:] = (value for value in nums if value != num)
#         nums[k] = num
#         k = k + 1



nums = [1,1,2]
k = 0

for i in range(1,len(nums)):
    if nums[k] != nums[i]:
        k += 1
        nums[k] = nums[i]
print(nums)

# for x in nums:
#     if x != val:    
#         nums[k] = x
#         k += 1
# return k

# print(nums)


