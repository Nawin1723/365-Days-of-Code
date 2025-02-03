class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        a=a[::-1]
        return ' '.join(a)
