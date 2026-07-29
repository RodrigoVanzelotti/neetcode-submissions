class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_lenght = 0
        s_len = len(s)

        if len(set(s)) == 1: return 1

        for i in range(s_len):
            if i == s_len: break
            temp_counter = 1

            for j in range(i+1, s_len):
                if s[j] in s[i:j]: break
                
                temp_counter += 1
                if temp_counter > substring_lenght:
                    substring_lenght = temp_counter

        
        return substring_lenght