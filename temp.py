from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count=0
        j=0
        for i in range(len(nums)):
            if nums[i]==0:
                k-=1
            
            if (k<0):
                if nums[j]==0:
                    k+=1

                j+=1
        count=i-j+1
            
        return count

# Test case
solution = Solution()
nums = [1, 1, 1, 0, 0, 0]
k = 2
result = solution.longestOnes(nums, k)
print(result)
