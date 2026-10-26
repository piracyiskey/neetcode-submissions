class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxLeft =[]
        maxRight = []
        max_left = 0
        max_right = 0

        for i in range(len(height)):
            if i == 0:
                maxLeft.append(0)
            else:
                max_left = max(max_left, height[i - 1])
                maxLeft.append(max_left)
        
        for i, n in reversed(list(enumerate(height))):
            if i == len(height) - 1:
                maxRight.append(0)
            else:
                max_right = max(max_right, height[i + 1])
                maxRight.append(max_right)
        maxRight.reverse()
        
        for i in range(len(height)):
            water = min(maxLeft[i], maxRight[i]) - height[i]
            if water < 0:
                water = 0
            res += water
        return res
