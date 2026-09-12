class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            number = nums[i]

            needed = target - number

            if needed in seen:
                return [seen[needed], i]

            seen[number] = i