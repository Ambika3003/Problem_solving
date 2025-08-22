class Solution:
    def getRow(self, rowIndex):
        ans=[[1],[1,1]]
        if rowIndex==0:
            return ans[0]
        elif rowIndex==1:
            return ans[1]
        else:
            n=2
            while(n<=rowIndex+1):
                a=ans[n-1]
                b=[1,1]
                i,j=0,1
                while(i<j and j<len(a)):
                    b.insert(j,a[i]+a[j])
                    i+=1
                    j+=1
                ans.append(b)
                n+=1
        return ans[rowIndex]
rowIndex=3
s=Solution()
res=s.getRow(rowIndex=rowIndex)
print(res)

'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]'''
