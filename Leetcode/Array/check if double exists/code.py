arr = [-2,-4,0,10,-19,4,6,-8]
# for num in arr:
#     temp = num
#     for num1 in arr:
#         if num1 == 0:
#             continue
#         if ((temp / num1) == 2):
#             print(True)
#         else:
#             print(False)

# def functiona(array):
#     for i in range(len(array)):
#         temp = array[i]
#         for num in array:
#             if 2*num == temp:
#                 return True
#     return False

# Solution 1 (Which involves two for loops)
if arr.count(0) == 1:
    arr.remove(0)

for i in range(len(arr)):
        temp = arr[i]
        for num in arr:
            if 2*num == temp:
                print(f"{2*num} == {temp}")

                print(True)
print(False)


# Solution 2 (which involves set)

arr_set = set()

for num in arr:
    if num*2 in arr_set or num/2 in arr_set:
        print(True)
    arr_set.add(num)
print(False)


