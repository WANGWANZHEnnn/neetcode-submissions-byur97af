class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)

        if n != m : return False

        return sorted(s) == sorted(t)

        
        