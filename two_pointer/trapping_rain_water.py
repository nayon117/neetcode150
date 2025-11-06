class Solution:
    def trap(self, h: List[int]) -> int:
        l, r = 0, len(h) - 1
        leftmax = rightmax = water = 0
        while l < r:
            if h[l] < h[r]:
                if h[l] >= leftmax:leftmax = h[l]
                else: water += leftmax - h[l]
                l += 1
            else:
                if h[r] >= rightmax: rightmax = h[r]
                else: water += rightmax - h[r]
                r -= 1
        return water
