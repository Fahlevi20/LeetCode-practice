class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msa = nums[0]
        curSum = 0

        for n in nums:
            if curSum <0:
                curSum = 0
            curSum +=n
            msa = max(msa,curSum)
        return msa        
