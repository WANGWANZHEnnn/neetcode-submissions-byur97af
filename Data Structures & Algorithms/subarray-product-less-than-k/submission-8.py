class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        res = 0
        n  = len(nums)
        l = 0
        pro = 1

        for r in range(n):
            pro *= nums[r]
            while l <= r and pro >= k:
                pro //= nums[l]
                l +=1

            res += (r-l +1)

        return res

 


        
                    






        

        