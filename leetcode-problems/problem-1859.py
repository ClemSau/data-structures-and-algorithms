# 1859.

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([x[:-1] for x in sorted(s.split(), key=lambda x:x[-1])])