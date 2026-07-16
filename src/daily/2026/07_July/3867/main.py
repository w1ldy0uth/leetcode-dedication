from math import gcd
from typing import List


class Solution:
  def gcdSum(self, nums: List[int]) -> int:
    """
    3867. Sum of GCD of Formed Pairs

    Build prefixGcd[i] = gcd(nums[i], running max so far), sort it, then pair
    smallest with largest, next-smallest with next-largest, etc. (two pointers
    from both ends), summing gcd of each pair. The odd middle element (if any)
    is skipped.

    Time: O(n log n)
    Space: O(n)
    """
    prefix_gcd = []
    running_max = 0
    for x in nums:
      running_max = max(running_max, x)
      prefix_gcd.append(gcd(x, running_max))

    prefix_gcd.sort()

    total = 0
    left, right = 0, len(prefix_gcd) - 1
    while left < right:
      total += gcd(prefix_gcd[left], prefix_gcd[right])
      left += 1
      right -= 1

    return total


print(Solution().gcdSum([2, 6, 4]))      # 2
print(Solution().gcdSum([3, 6, 2, 8]))   # 5
