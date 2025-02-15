class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        b = s.strip().split(" ")
        c = len(b[-1])
        return c
