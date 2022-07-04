class Solution:
    def isValid(self, s: str) -> bool:
        pattern = {"{": "}", "(": ")", "[": "]"}
        stack = []
        
        for char in s:
            if char in pattern:
                stack.append(char)
            else:
                if len(stack) == 0 or pattern[stack.pop()] != char:
                    return False
        return len(stack) == 0

# s = "([(]){}{})"
# bracket_dict = {'(':')', '[': ']','{':'}'}
# list_ = list(s)
# # mid_l, mid_r = len(list_)//2 - 1, len(list_)//2
# # print(list_[mid_l], mid_l)
# # print(list_[mid_r], mid_r)
# # print(list(s))
# mid_l, mid_r = len(list_)//2 - 1, len(list_)//2


# for _ in range(len(list_)//2):
#     # for bracket in list_:
#     # print("In While loop")
    
#     left_bracket = list_[mid_l]
#     # print(f"left bracket is {left_bracket}")
       
#     if bracket_dict.get(left_bracket):
#         r_bracket = list_[mid_r]
#         right_bracket = bracket_dict.get(left_bracket)

#         # print(f"left bracket is {left_bracket}")
#         print(f"r bracket is {r_bracket}")
        
#         print(f"right bracket is {right_bracket}")


#         if r_bracket == right_bracket:
#             print("equal")
#             print(f"r bracket is {r_bracket}")
        
#             print(f"right bracket is {right_bracket}")

#             del list_[mid_l]
#             del list_[mid_r]
#             mid_l -= 1
#             mid_l += 1
#             print(list_)
#         else:
#             mid_r += 1

#         if len(list_)==0:
#             print(True)
#             break
#     else:
#         mid_l -= 1
    

