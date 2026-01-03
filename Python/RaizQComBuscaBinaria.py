class Solution:
    def mySqrt(self, num: int) -> int:
        from math import floor
        if num == 0:
            return 0
        if num == 1:
            return 1

        if num > 1:
            min, max = 0, num
        else:
            min, max = 0, 1
        result = 0
        
        while abs(num - result) > 0.01:
            meio = (min + max) / 2
            result = meio * meio
            
            if result > num:
                max = meio
            else:
                min = meio
            
        meio = round(meio, 2)
        
        if meio ** 2 > num:
            meio -= 1
            
        return floor(meio)
    
s = Solution()
print(s.mySqrt(2147395599))
