# 7. Reversed Integer

class Solution:
    def reverse(self, x: int) -> int:
        z = list(reversed(str(x)))
        if set(z) == set(['0']):
            return 0
        
        negative = False
        if z[-1] == '-':
            negative = True
            del z[-1]
            
        i = 0
        while z[i] == '0':
            i += 1
            
        if negative:
            z = -int(''.join(z[i:]))
        else:
            z = int(''.join(z[i:]))
            
        if (-2**31 < z) and (z < 2**31 -1):
            return z
        
        return 0
