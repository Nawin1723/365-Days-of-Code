class Solution:
    def divide(self, a: int, b: int) -> int:
        if a == -2**31 and b == -1:
            return 2**31 - 1
        neg = (a < 0) != (b < 0)
        a, b = abs(a), abs(b)
        c = 0
        for i in range(31, -1, -1):
            if a >= (b << i):
                a -= b << i
                c += 1 << i
        return -c if neg else c
