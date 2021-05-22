# 1409.

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        permutations = [i for i in range(1, m+1)]
        result = []
        for i in range(len(queries)):
            index = permutations.index(queries[i])
            result.append(index)
            permutations.insert(0, permutations.pop(index))
        return result
            