from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped_values = {}
        temp_str = ''
        for i in nums:
            for single_digit in str(i):
                for index, value in enumerate(mapping):
                    if index == int(single_digit):
                        temp_str += str(value)
            mapped_values[temp_str] = i
            temp_str = ''
        temp_res = dict(sorted(mapped_values.items()))
        print(temp_res)
        return list(temp_res.values())



sol = Solution()
print(sol.sortJumbled([5,6,8,7,4,0,3,1,9,2], [7686,97012948,84234023,2212638,99]))
