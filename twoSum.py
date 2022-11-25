class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return None

# another hashmap solution
# class Solution(object):
# def twoSum(self, nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     hashmap = {}

#     for i, n in enumerate(nums):
#         val = target - n
#         if val in hashmap:
#             return [hashmap[val], i]
#         else:
#             hashmap[n] = i
