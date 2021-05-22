# 1313.

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(int(len(nums)/2)):
            for j in range(nums[i*2]):
                result.append(nums[i*2+1])
        return result