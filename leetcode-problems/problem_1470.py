# 1470. Shiffle the Array

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_index = []
        for i in range(n):
            shuffled_index.append(i)
            shuffled_index.append(i+n)
        return [nums[i] for i in shuffled_index]
        