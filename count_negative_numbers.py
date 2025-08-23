#Count Negative Numbers in a Sorted Matrix
class Solution:
    def countNegatives(self,grid):
        r=len(grid)
        c=len(grid[0])
        ans=0
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                if grid[i][j]<0:
                    ans+=1
                else:
                    break
        return ans
grid=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
s=Solution()
ans=s.countNegatives(grid)
print(ans)

'''
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0'''
