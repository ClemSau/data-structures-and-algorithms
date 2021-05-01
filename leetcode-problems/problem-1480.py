# 1480. Running Sum of 1D Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rsums = [0]
        for i in nums:
            rsums.append(rsums[-1]+i)
        del rsums[0]
        return rsums