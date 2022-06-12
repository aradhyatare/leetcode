arr = [400]
# print(len(arr))

def replaceElements(arr):
    for i in range(len(arr)):
        if i == len(arr)-1:
            arr[i] = -1
        else:
            arr[i] = max(arr[i+1:])
    return arr