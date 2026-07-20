class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        csum = nums[0]
        for i in range(1, len(nums)):
            csum = max(nums[i], csum+nums[i])
            maxsum = max(maxsum,csum)
        return maxsum