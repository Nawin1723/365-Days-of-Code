class Solution:
    def removeElement(self, ab, c):
        k = 0
        for i in range(len(ab)):
            if ab[i] != c:
                ab[k] = ab[i]
                k += 1
        return k
