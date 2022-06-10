nums = [1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
i = 0
n = 0
numberof1 = []
# while (i < len(nums)-1):
#     print(i)
#     while nums[i] == 1:
#         print(nums[i])
#         print("in while loop")
#         n += 1
        
#         if nums[i] == 0:
#             print(nums[i])
#             print("in if loop")
#             i = i + 1
#             break
#         i = i + 1
#     numberof1.append(n)
# print(len(nums))
for num in nums:
    i += 1
    if num == 1:
        n += 1
        # print(i)
    if num == 0 or i == len(nums):
        numberof1.append(n)
        n = 0
print(max(numberof1))