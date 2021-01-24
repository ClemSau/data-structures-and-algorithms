# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = 0 # Current max
        i = 0 # Index of the character for the current substring 
        seen = set() # Set of the seen characters
        
        for j, c in enumerate(s):
            while c in seen:
                seen.remove(s[i])
                i += 1
            
            seen.add(c)
            k = max(k, j - i + 1)
            
        return k