class Solution:
    def dailyTemperatures(self, temperatures):

        res = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t >stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = (i - stackI)
            stack.append([t,i])
        
        return res
#         result_list = []
#         max_temp = temperatures[0]
#         count = 0
#         for temp in range(1,len(temperatures)):
#             if max_temp > temperatures[temp]:
#                 count += 1
#             else:
#                 max_temp = temperatures[temp]
#                 result_list.append(count)

#         print(result_list)

#             # stack.append(temperatur)


# temperatures = [73,74,75,71,69,72,76,73]
# temperatures = temperatures[::-1]
# # print(temperatures.pop())
# print(temperatures.pop())
# print(temperatures)
# print(temperatures.pop())
# print(temperatures)

# # print(temperatures[1])
# # result_list = []
# # # max_temp = temperatures[0]
# # count = 1
# # i = 0
# # # stack = [max_temp]
# # while len(temperatures) != 0:
# #     max_temp = temperatures.pop()
# #     print(f"Max temperature is {max_temp} at index {i}")
# #     i += 1
# #     for temp in range(0,len(temperatures)):
# #         if max_temp < temperatures[temp]:
# #             # print(f"The temperature is {temperatures[temp]}")
# #             # stack.append(temperatures[temp])
# #             result_list.append(count)
# #             count = 1
# #             break
# #         elif max_temp > temperatures[temp]:
# #             count += 1
# # print(result_list)

# # # for temp in range(0,len(temperatures)):
# # #     for temp1 in range(1,len(temperatures)):
# # #         if temperatures[temp] > temperatures[temp1]:
# # #             count += 1
# # #         else:
# # #             max_temp = temperatures[temp]
# # #             result_list.append(count)
# # #             count = 1
# # #     diff = len(temperatures) - len(result_list)
# # #     for _ in range(diff):
# # #         result_list.append(0)

# # # print(result_list)