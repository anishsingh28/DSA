class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s) 
        n = len(s)

        
        for i in range(0, n, 2 * k): 
           
            start_reverse = i  

            
            end_reverse = min(i + k - 1, n - 1) 

            
            left = start_reverse
            right = end_reverse
            while left < right:
                
                s[left], s[right] = s[right], s[left]
                
                left += 1
                right -= 1
        
       
        return "".join(s)