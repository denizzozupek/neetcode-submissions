class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        whats_seen = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in whats_seen:
                return [whats_seen[diff], index]
            whats_seen[num] = index
