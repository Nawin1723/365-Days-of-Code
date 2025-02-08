class Solution:
    def spiralOrder(self, matrix):
        a, b = 0, 0
        c, d = len(matrix), len(matrix[0])
        res = []

        while a < c and b < d:
            for i in range(b, d):  
                res.append(matrix[a][i])
            a += 1

            for i in range(a, c):  
                res.append(matrix[i][d - 1])
            d -= 1

            if a < c:
                for i in range(d - 1, b - 1, -1):  
                    res.append(matrix[c - 1][i])
                c -= 1

            if b < d:
                for i in range(c - 1, a - 1, -1):  
                    res.append(matrix[i][b])
                b += 1

        return res
