"""
https://leetcode.com/problems/two-sum/
"""


class Solution(object):
    def twoSum(self, nums, target):
        # Two-pass Hash Table o(n)
        table = {}
        for i in range(len(nums)):
            table[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in table and table.get(complement) != i:
                return [i, table.get(complement)]

        # i = 0
        # j = 1
        # res = [i, j]
        # while nums[res[0]] + nums[res[1]] != target:
        #     if j == len(nums) - 1:
        #         i += 1
        #         j = i + 1
        #     else:
        #         j += 1
        #     res = [i, j]
        # return res


if __name__ == '__main__':
    s = Solution()
print(s.twoSum([1, 2, 3], 4))
