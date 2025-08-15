#Power of Four
'''Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        i=0
        while(i>=0):
            if n==pow(4,i):
                return True
            elif n<pow(4,i):
                return False
            else:
                i+=1
n=7
s=Solution()
ans=s.isPowerOfFour(n=n)
print(ans)
