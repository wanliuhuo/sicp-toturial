class Solution(object):
    def posPow(self, x, n):
        result = 1
        copy = x
        while n > 0:
            if n%2 == 1:
                result = result * copy
            copy = copy*copy
            n = n/2
        return result

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n > 0:
            return self.posPow(x, n)
        if n < 0:
            return 1.0/(self.posPow(x, -n)*1.0)


        
