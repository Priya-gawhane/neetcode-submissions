class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keys = {}

        for num in nums:
            if num in keys:
                return True
            keys[num] = True
        return False