class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        countset = set()
        for num in nums:
            if num in countset:
                return True
            countset.add(num)
        
        return False
            

