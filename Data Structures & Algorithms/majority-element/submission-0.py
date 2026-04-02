class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for num in nums:
            cnt = sum(1 for i in nums if i == num)
            if cnt > n//2:
                return num

        