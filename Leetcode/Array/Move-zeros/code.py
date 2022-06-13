nums = [0,1,0,3,12]

j = 0
for i in range(len(nums)):
    if nums[i]==0:
        nums.remove(0)
        nums.append(0)

print(nums)


nums = [0,1,0,3,12]

j = 0
for i in range(len(nums)):
    if (nums[i] != 0):
        print(i)
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
print(nums)
