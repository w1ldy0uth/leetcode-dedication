from typing import List


class Solution:
  def maximumProduct(self, nums: List[int]) -> int:
    """
    628. Maximum Product of Three Numbers

    Find max product of three numbers by tracking top 3 max and bottom 2 min values.

    Time: O(n)
    Space: O(1)
    """
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')
    for i in nums:
      if i > max1:
        max1, max2, max3 = i, max1, max2
      elif i > max2:
        max2, max3 = i, max2
      elif i > max3:
        max3 = i
      if i < min1:
        min1, min2 = i, min1
      elif i < min2:
        min2 = i
    return max(max1 * max2 * max3, min1 * min2 * max1)


print(Solution().maximumProduct([1, 2, 3]))  # 6
print(Solution().maximumProduct([1, 2, 3, 4]))  # 24
print(Solution().maximumProduct([-1, -2, -3]))  # -6
