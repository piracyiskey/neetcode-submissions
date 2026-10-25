class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        zeroCount = 0

        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                product *= num
        
        for num in nums:
            if zeroCount > 1:
                res.append(0)
            elif zeroCount == 1:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(int(product * pow(num, -1)))
        return res
