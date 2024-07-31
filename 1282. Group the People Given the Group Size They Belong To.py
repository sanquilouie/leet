from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []
        for i in range(len(groupSizes)):
            if groupSizes[i] not in groups:
                groups[groupSizes[i]] = []
            groups[groupSizes[i]].extend([i])

        for key, values in groups.items():
            for i in range(0, len(values), key):
                result.append(values[i:i + key])

        return result


sol = Solution()
print(sol.groupThePeople([3,3,3,3,3,1,3]))
