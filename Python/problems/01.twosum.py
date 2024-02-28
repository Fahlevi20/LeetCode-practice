class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        terlihat = {} #make dictionary
        for i in range(len(nums)):
            pembeda = target-nums[i] #make different from num subtract from target
            if pembeda in terlihat: # if pembeda value in terlihat value
                return [terlihat[pembeda],i] #return terlihat value and index i (from nums)

            else:
                terlihat[nums[i]] = i 