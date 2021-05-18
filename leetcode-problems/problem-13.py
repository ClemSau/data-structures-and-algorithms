# .13

class Solution:
    def romanToInt(self, s: str) -> int:
        ROMANS = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
        
        result = 0
        value = 0
        for letter in s[::-1]:
            pre_value = value
            value = ROMANS.get(letter)
            if value < pre_value:
                result -= value
            else:
                result += value
        return result 
