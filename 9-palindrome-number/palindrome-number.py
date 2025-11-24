class Solution:
    def isPalindrome(self, x: int) -> bool:

        s = str(x)
        rev = ""
        for i in s:
             rev = i + rev
        
       
        if (rev==s):
            return True
        else:
            return False
        
    