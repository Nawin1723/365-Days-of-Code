from typing import List

class Solution:
    def longestCommonPrefix(self, a: List[str]) -> str:
        if not a:
            return ""
        
        p = a[0]
        
        for i in a[1:]:
            while not i.startswith(p):
                p = p[:-1]
                if not p:
                    return ""
        
        return p
