from typing import List
from math import gcd


class Solution:
  """
  1979. Find Greatest Common Divisor of Array

  Simply find the min and max of the array, then return their GCD.

  Time: O(n + log(mn))
  Space: O(1)
  """
  def findGCD(self, nums: List[int]) -> int:
    mn, mx = min(nums), max(nums)
    return gcd(mn, mx)


print(Solution().findGCD([2, 5, 6, 9, 10]))  # 2
print(Solution().findGCD([7, 5, 6, 8, 3]))   # 1
print(Solution().findGCD([3, 3]))            # 3
