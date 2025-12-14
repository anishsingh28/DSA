class Solution:
    def minimumFlips(self, n: int) -> int:
        binary =bin(n)[2:]
        print(binary)
        i=0
        j=len(binary)-1
        count=0
        while i<j:
            if binary[i]!=binary[j]:
                count+=2
            i+=1
            j-=1
        return count
        
        