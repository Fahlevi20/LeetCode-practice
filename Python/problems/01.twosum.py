class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bracket={}
        for i, number in enumerate(nums):
            diff = target-number
            if diff in bracket:
                return [bracket[diff],i]
            bracket[number] = i
        return
