nums = [0,0,1,1,1,2,2,3,3,4]

length = len(nums)

# for i in range(len(arr)):
#     if arr[i] == arr[i+1]:
#         arr.remove(i)
#         length -= 2

# print(arr)

j = 0
for i in range(1,len(nums)):
    if nums[j] != nums[i]:
        j += 1
        nums[j] = nums[i]
print(j+1)

print(nums)


# public int removeDuplicates(int[] nums) {
        
#         // The initial length is simply the capacity.
#         int length = nums.length;
        
#         // Assume the last element is always unique.
#         // Then for each element, delete it iff it is
#         // the same as the one after it. Use our deletion
#         // algorithm for deleting from any index.
#         for (int i = length - 2; i >= 0; i--) {
#             if (nums[i] == nums[i + 1]) {
#                 // Delete the element at index i, using our standard
#                 // deletion algorithm we learned.
#                 for (int j = i + 1; j < length; j++) {
#                     nums[j - 1] = nums[j];
#                 }
#                 // Reduce the length by 1.
#                 length--;
#             }
#         }
#         // Return the new length.
#         return length;
#     }