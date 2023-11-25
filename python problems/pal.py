class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0 or (x!=0 and int(math.fmod(x,10))==0)):
            return False
        reversed =0 
        while(x>reversed):
            l =int(math.fmod(x,10))
            reversed = reversed*10 + l
            x= int(x/10)
        return reversed == x or int(reversed/10)==x