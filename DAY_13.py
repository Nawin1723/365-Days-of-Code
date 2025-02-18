class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        b = {')': '(', '}': '{', ']': '['}
        for i in range(len(s)):
            if s[i] in b:
                if not a or a.pop() != b[s[i]]:
                    return False
            else:
                a.append(s[i])
        return not a
