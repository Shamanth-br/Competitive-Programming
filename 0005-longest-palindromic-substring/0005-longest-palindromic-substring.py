class Solution:
    def expandFromTheMiddle(self, s, l, r):
        n = len(s)
        while l-1 >= 0 and r+1 < n and s[l-1] == s[r+1]:
            l -= 1
            r += 1
        return (l, r)
        
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ansLength = 0
        ansStartIdx = 0

        for i in range(n):
            cand = [self.expandFromTheMiddle(s, i, i)] # Odd palindrome
            if i + 1 < n and s[i] == s[i+1]: # Even palindrome
                cand.append(self.expandFromTheMiddle(s, i, i+1))

            for l, r in cand:
                if r - l + 1 > ansLength:
                    ansLength = r - l + 1
                    ansStartIdx = l
        
        return s[ansStartIdx : ansStartIdx + ansLength]
