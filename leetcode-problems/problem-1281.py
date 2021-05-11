# 1281

class Solution:    
    def get_product(self, n):
        product = 1
        while(n != 0):
            product = product*(floor(n%10))
            n = floor(n/10)
        return product
    
    def get_sum(self, n):
        _sum = 0
        while(n != 0):
            _sum = _sum + (floor(n%10))
            n = floor(n/10)
        return _sum
            
    def subtractProductAndSum(self, n: int) -> int:
        return self.get_product(n) - self.get_sum(n)