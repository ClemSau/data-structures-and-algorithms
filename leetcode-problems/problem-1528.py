# 1528.

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ""
        for i in range(len(indices)):
            result += s[indices.index(i)]
        return result
        