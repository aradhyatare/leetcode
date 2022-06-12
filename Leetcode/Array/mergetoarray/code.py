nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

del nums1[m:]
print(nums1)
nums2 = nums2[:n]

for i in nums2:
    nums1.append(i)
nums1.sort()
print(nums1)
print(nums2)