class Solution:
    def countPrefixSuffixPairs(self, s: List[str]) -> int:
        c=0
        for i in range(len(s)):
            b=list(s[i])
            for j in range(i+1,len(s)):
                a=list(s[j])
                
                if b == a[:len(s[i])] and b==a[-len(s[i]):]:
                    c+=1
        return c
