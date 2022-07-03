# class Solution:
#     def isValid(self, s: str) -> bool:
#         list_ = list(s)
#         mid_l, mid_r = len(list_)/2 - 1, len(list_)/2 + 1
#         print(mid_l)
#         print(mid_r)
#         pass

s = "()[]{}{}"
bracket_dict = {'(':')', '[': ']','{':'}'}
list_ = list(s)
# mid_l, mid_r = len(list_)//2 - 1, len(list_)//2
# print(list_[mid_l], mid_l)
# print(list_[mid_r], mid_r)
# print(list(s))
mid_l, mid_r = 0
while mid_l and mid_r in range(len(list_)):
    # for bracket in list_:
    mid_l, mid_r = len(list_)//2 - 1, len(list_)//2

    left_bracket = list_[mid_l]
    r_bracket = list_[mid_r]
    right_bracket = bracket_dict.get(left_bracket)


    if r_bracket == right_bracket:
        del list_[mid_l]
        del list_[mid_r]
        mid_l -= 1
        mid_l += 1
    else:
        mid_r += 1

    if len(list_)==0:
        print(True)
        break
    

