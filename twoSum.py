class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # O(N) time using hash map
        map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff],i]
            map[n] = i
        return

