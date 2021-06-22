# 9.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = int(floor(len(str(x))/2))
        for i in range(y):
            if str(x)[i] != str(x)[-(i+1)]:
                return False
        return True
      
