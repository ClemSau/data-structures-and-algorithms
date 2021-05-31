# 1684

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for word in words:
            if set(word).issubset(set(allowed)):
                count += 1
        return count
        