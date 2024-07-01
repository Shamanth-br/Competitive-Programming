class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i,vowel_count,size = 0,0,len(s)
        vowels = ('a','e','i','o','u')
        for c in s[i:i+k]:
            if c in vowels:
                vowel_count += 1
        i,j,count = 0,k,vowel_count
        while(j < size):
            if s[j] in vowels and s[i] not in vowels:
                count += 1 
            if s[j] not in vowels and s[i] in vowels:
                count -= 1
            if count > vowel_count:
                vowel_count = count
            i += 1
            j += 1
        return vowel_count 