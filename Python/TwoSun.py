class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        v = {}
        for i, num in enumerate(nums):
            
            f = target - num
            
            if f in v:
                return [v[f], i]
            
            v[num] = i
        
n = Solution()
print(n.twoSum([1, 1, 2, 3], 4))
