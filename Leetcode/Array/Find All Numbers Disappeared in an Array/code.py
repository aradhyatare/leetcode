nums = [3,11,8,16,4,15,4,17,14,14,6,6,2,8,3,12,15,20,20,5]
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,32]
# dusri_list = [x for x in range(1,max(nums)+1)]
# nums = set(nums)
# nums.sort()
# print(dusri_list)
loop_range = len(nums)
if loop_range > 10:
    nums = set(nums)
    loop_range= max(nums)
print(max(nums))

answer = []
for i in range(1,loop_range + 2):
    if i not in nums:
        answer.append(i)
print(answer)