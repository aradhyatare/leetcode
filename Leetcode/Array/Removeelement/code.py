nums = [3,2,2,3,3,3,3,4,3]
length = len(nums)
val = 3
count = 0
i = 0
# nums = list(filter((val).__ne__,nums))

# print(count)
# print(nums)

# nums = [value for value in nums if value != val]
# print(nums)

# for i in range(length):
#     print(nums[-1])
#     if (nums[-1] == val):
#         print("In while loop")
#         del nums[-1]
#         length -= 2
#     if nums[i]==val:
        
#         nums[i] = nums[-1]
nums[:] = (value for value in nums if value != val)
        
print(nums)
