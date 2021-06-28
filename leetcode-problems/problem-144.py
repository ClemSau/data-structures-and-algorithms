# 144.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        reversed_words = list(map(lambda x: x[::-1], words))
        return " ".join(reversed_words).strip()
      
