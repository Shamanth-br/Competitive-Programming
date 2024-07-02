class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1,l2 = len(str1),len(str2)
        multiple = []
        l_key = min(l1,l2)
        for i in range(1,l_key+1):
            if l1 % i == 0 and l2 % i == 0:
                multiple.append(i) 
                
        for val in multiple[::-1]:
            if str1[:val] * int(l1/val) == str1 and str1[:val]* int(l2/val) == str2:
                return str1[:val]
        return ''

