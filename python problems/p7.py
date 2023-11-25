class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min = -2147483648
        max = 2147483647
        reversed  = 0
        while x:
            l= int(math.fmod(x,10))

            if(reversed > int(max/10) or (reversed == int(max/10) and l > 7)):
                return 0
            if(reversed < int(min/10) or (reversed == int(min/10) and l<-8)):
                return 0
            x= int(x/10)
            reversed = reversed * 10 + l