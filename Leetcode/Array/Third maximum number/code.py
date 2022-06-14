nums = [-1,2,3,-2]

nums.sort()
# print(nums)
temp = []

for x in nums:
    if x not in temp:
        temp.append(x)

# print(temp)
# j = 0
# for i in range(1,len(nums)-2):
#     if nums[i] == nums[j]:
#         nums.remove(nums[j])
#     j += 1

# print(nums)



if len(temp) <=2:
    print(temp[-1])
else:
    print(temp[-3])



#Second approach

nums = set(nums)

        # Find the maximum.
maximum = max(nums)

# Check whether or not this is a case where
# we need to return the *maximum*.
if len(nums) < 3:
    print(maximum)

# Otherwise, continue on to finding the third maximum.
nums.remove(maximum)
second_maximum = max(nums)
nums.remove(second_maximum)
print(max(nums))

