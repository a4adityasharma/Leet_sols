class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        a = sum(nums)
        # b = a//k
        return a - (a//k)*k