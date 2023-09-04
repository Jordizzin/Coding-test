def solution(s1, s2):
#     answer = 0

#     for val in s1:
#         if val in s2:
#             answer += 1
            
    return len(set(s1)&set(s2))