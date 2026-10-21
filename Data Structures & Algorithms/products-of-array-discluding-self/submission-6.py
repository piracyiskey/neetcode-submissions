class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        zero = 0

        for num in nums:
            if num == 0:
                zero += 1
            else:
                prod *= num
        
        for num in nums:
            if zero > 1:
                res.append(0)
            elif zero == 1:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(int(prod*pow(num, -1)))
        return res
