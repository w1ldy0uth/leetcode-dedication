from typing import List


class Solution:
  def leftRightDifference(self, nums: List[int]) -> List[int]:
    """
    2574. Left and Right Sum Differences

    Single pass with a running left sum; right sum = total - left - nums[i],
    avoiding the need to build explicit leftSum and rightSum arrays.
    """
    total = sum(nums)
    ans, left = [], 0
    for n in nums:
      ans.append(abs(left - (total - left - n)))
      left += n
    return ans


print(Solution().leftRightDifference([10, 4, 8, 3]))  # [15,1,11,22]
print(Solution().leftRightDifference([1]))             # [0]
