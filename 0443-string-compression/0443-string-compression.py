class Solution:
    def compress(self, chars: List[str]) -> int:
        i,j,size = 0,0,len(chars)
        compressed_str = ""
        while(i < size):
            j = 0
            while(i+j < size  and chars[i] == chars[j+i]):
                j += 1
            if j  == 1:
                compressed_str += chars[i]
            else:
                compressed_str = compressed_str + chars[i] + str(j) 
            i += j

        i = 0
        print(compressed_str)
        for ch in list(compressed_str):
            chars[i] = ch
            i += 1 
        return len(compressed_str)