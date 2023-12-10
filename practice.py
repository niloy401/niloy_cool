class Solution(object):
  def smallestRangeI(self, nums, k):
    maxNum = max(nums)
    minNum = min(nums)
    return max(0, maxNum-k-minNum-k)

obj = Solution()
result = obj.smallestRangeI([1,23,6], 3) 
print(result)