nums = [12,345,2,6,7896]
even = 0

# First way using for and while loops
for num in nums:
    count = 0
    while(num > 0):
        count += 1
        num = num//10 
    if (count % 2) == 0:
        even += 1
    if len(str(num))%2==0:
        even += 1
print(even)


# Second way using python's len function
for num in nums:
    if len(str(num))%2==0:
        even += 1
print(even)




