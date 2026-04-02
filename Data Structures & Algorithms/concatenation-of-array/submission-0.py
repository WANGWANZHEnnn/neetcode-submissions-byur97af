class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.copy()

        return nums + nums.copy()
        