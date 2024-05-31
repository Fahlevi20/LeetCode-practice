class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bucket = {}
        for i in range(len(nums):
            diff = target-nums[i]
            if diff in bucket:
                return [bucket[diff],i]
            bucket[nums[i]=i
