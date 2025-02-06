class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        a = 0
        b = 0
        n = len(s)
        
        for i in range(n - 1, -1, -1):
            v = d[s[i]]
            if v < b:
                a -= v
            else:
                a += v
            b = v
        return a
