class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        def canFinish(k):
            total_hour = 0
            for pile in piles:
                total_hour += (pile + k -1) // k
            return total_hour <= h

        
        l = 1
        r  = max(piles)

        while l <= r:
            mid = (l + r) // 2

            if canFinish(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


        
            

        