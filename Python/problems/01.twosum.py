class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vessel = {}

        for egg in range(len(nums)):
            distinct = target - nums[egg]
            if distinct in vessel:
                return [vessel[distinct],egg]
            vessel[nums[egg]]=egg
        return []
