from typing import List


class Solution:
  def maxTotalValue(self, nums: List[int], k: int) -> int:
    """
    3689. Maximum Total Subarray Value I

    The best single subarray value is global_max - global_min (achieved by the
    full array or any subarray containing both extremes). Since we can reuse the
    same subarray k times, the answer is k * (max - min).
    """
    return k * (max(nums) - min(nums))


print(Solution().maxTotalValue([1, 3, 2], 2))    # 4
print(Solution().maxTotalValue([4, 2, 5, 1], 3)) # 12
print(Solution().maxTotalValue([5], 3))           # 0
