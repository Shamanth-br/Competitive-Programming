class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        i,count = len(s) - 1,0
        while(i >= 0):
            if s[i] == '*':
                count += 1
            elif count != 0:
                count -= 1
            else:
                ans.append(s[i])
            i -= 1
        return ''.join(ans[::-1])