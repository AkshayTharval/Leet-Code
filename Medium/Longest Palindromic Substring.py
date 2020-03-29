class Solution:
    def longestPalindrome(self, s):
        m = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j-i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m
    
    
#     def longestPalindrome(self, s):

#         if len(s) == 1 or len(s) == 0:
#             return s

#         if len(s) == 2 and s[0] != s[1]:
#             return s[0]

#         if len(set(s)) == 1:
#             return s

#         max_len = 0
#         current_pal = ''

#         for i in range(len(s)):
#             current_letter = s[i]

#             if s[i] not in s[i+1:]:
#                 continue
#             next_occ = s[i+1:][::-1].index(s[i])
#             next_occ = len(s[i+1:]) - next_occ -1

#             if s[i:i+next_occ+2] == s[i:i+next_occ+2][::-1] and i+next_occ+2 - i > max_len:
#                 current_pal = s[i:i+next_occ+2]
#                 max_len = i+next_occ+2 - i

#         if current_pal == '':
#             current_pal = s[0]
#         return current_pal


        
        
            
        