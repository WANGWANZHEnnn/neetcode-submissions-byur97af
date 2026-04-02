class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        
        prevMap = {}

        for i , nums in enumerate(nums):
            diff = target - nums

            if diff in prevMap:
                return [prevMap[diff],i]

            prevMap[nums] = i


        