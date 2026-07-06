class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # return min(abs(z-x),abs(z-y))
        p1 = abs(z-x)
        p2 = abs(z-y)
        if p1 == p2:
            return 0
        if p1<p2:
            return 1
        else:
            return 2