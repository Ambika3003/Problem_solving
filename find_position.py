#find first and last position of element in sorted array
class Solution:
    def searchRange(self,nums,target):
        if target in nums:
            a=nums.index(target)
            b=nums.count(target)
            if b==1:
                return [a,a]
            elif b==2:
                return [a,a+1]
            else:
                return [a,a+(b-1)]
        else:
            return [-1,-1]
nums=[5,7,7,8,8,10]
target=8
c=Solution()
res=c.searchRange(nums=nums,target=target)
print(res)

'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]'''
