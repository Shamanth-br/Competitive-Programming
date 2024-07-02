class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        d1,d2 = {},{}
        for ch in word1:
            d1[ch] = d1.get(ch,0) + 1
            if ch not in word2:
                return False
        for ch in word2:
            d2[ch] = d2.get(ch,0) + 1
        
        v1d,v2d = {},{}
        for val in d1.values():
            v1d[val] = v1d.get(val,0) + 1
        for val in d2.values():
            v2d[val] = v2d.get(val,0) + 1
        
        for key,value in v1d.items():
            if v2d.get(key,0) != value:
                return False
        return True