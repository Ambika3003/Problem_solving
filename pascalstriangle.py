#pascal's Triangle
class Solution:
    def generate(self, numRows):
        ans=[[1],[1,1]]
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return ans
        else:
            n=3
            while(n<=numRows):
                a=ans[n-2]
                b=[1,1]
                i,j=0,1
                while(i<j and j<len(a)):
                    b.insert(j,a[i]+a[j])
                    i+=1
                    j+=1
                ans.append(b)
                n+=1
        return ans
numRows=5
a=Solution()
b=a.generate(numRows=numRows)
print(b)

'''o/p:numsRows=5
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]'''

'''Pascal's Triangle
           1
          1  1
         1  2  1
        1  3  3  1
       1  4  6  4  1'''
