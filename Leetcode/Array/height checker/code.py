heights = [5,1,2,3,4]
temp_heights = sorted(heights)
count = 0
for i in range(len(heights)):
    if heights[i] != temp_heights[i]:
        count += 1
print(count)

