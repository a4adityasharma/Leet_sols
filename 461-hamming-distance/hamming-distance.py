class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = f"{x^y:b}"
        return sum(int(i) for i in z)