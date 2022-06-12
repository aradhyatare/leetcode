# In the code the approach was to find the point where elements in array are in the discending order.
# After getting the mid point we will check if the remaining array is in decending order or not 

arr = [0,1,2,3,4,5,6,7,8,9,1]

def mountainornot(arr):

    if len(arr) <3:
        return False
    mid_point = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1] :
            mid_point = i
        # if arr[i] == arr[i+1]:
        #     return False
        # else:
        #     mid_point = i
        #     break
        
    # print(mid_point)
    # print(arr[mid_point+1:])
    if mid_point ==0:
        return False
    temp_arr = arr[mid_point+1:]
    # print(len(temp_arr))
    for i in range(0,len(temp_arr)-1):
        if temp_arr[i] <= temp_arr[i+1]:
            return False
    return True
    # i = 0
    # while i<(len(temp_arr)-1):
    #     if temp_arr[i] > temp_arr[i+1]:
    #         print(f"{temp_arr[i]}>{temp_arr[i+1]}")
    #         # continue
    #     if temp_arr[i] == temp_arr[i+1]:
    #         return False
    #     i += 1
    # return True

# mountainornot(arr)
print(mountainornot(arr))
