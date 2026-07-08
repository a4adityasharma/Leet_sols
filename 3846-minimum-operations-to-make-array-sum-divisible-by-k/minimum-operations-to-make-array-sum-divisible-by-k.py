class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # a = sum(nums)
        # b = a//k
        return sum(nums) - (sum(nums)//k)*k