class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)
        res = []

        for i in range(n-1,-1,-1):
             res.append(s[i])

        for i in range(n):
            s[i] = res[i]
        


        

        