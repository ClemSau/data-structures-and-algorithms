# 1431. Kids With the greatest number of candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if extraCandies+c >= max(candies) else False for c in candies]
        