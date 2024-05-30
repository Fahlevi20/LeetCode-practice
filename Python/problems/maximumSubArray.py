class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msa = nums[0]
        curS= 0
        
        for n in nums:
            if curS < 0:
                curS=0
            curS+=n
            msa = max(msa,curS)
        return msa

        
