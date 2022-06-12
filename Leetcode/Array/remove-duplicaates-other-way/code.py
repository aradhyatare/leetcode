arr = [0,0,1,1,1,2,2,3,3,4]

length = len(arr)

for i in range(length-1):
    if arr[i] == arr[i+1]:
        arr.remove(i)
        length -= 1

print(arr)