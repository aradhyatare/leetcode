

# result = []

# for num in range(len(arr)):
#     print(arr[num])
#     if arr[num] == 0:
#         print(arr[:num+1])
#         arr[:num+1].append(0)
#         arr[:num+1].append(0)
#         print(arr[:num+1])
#     # num +=1
#     # result.append(num)
# print(arr[:length])
# print(arr)
# print(result[:len(arr)])
# temp = arr[:2].append(0) + arr[2:]
# # temp.append(0)
# print(temp)
# n = 0
# for i in range(length):
#     print(i)
#     if arr[i] == 0:
#         n += 1 
#         print(f'n={n}')
#         print(f'arr[i] = {arr[i]}')
#         print(arr[:i+n])
#         temp = arr[:i+n].append(0)
#         print(temp)
arr = [1,0,2,3,0,4,5,0]
length = len(arr)
# for i in range(length):
i = 0
while i < length: 
    if arr[i] == 0:
        arr.insert(i,0)
        i += 1 
    i += 1 
del arr[length:]
print(arr)