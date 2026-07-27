class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    """
    1464. Maximum Product of Two Elements in an Array

    Track two highest values by a single loop.

    Time: O(n)
    Space: O(1)
    """
    first = second = 0
    for num in nums:
      if num > first:
        first, second = num, first
      elif num > second:
        second = num
    return (first - 1) * (second - 1)


print(Solution().maxProduct([3, 4, 5, 2]))  # 12
print(Solution().maxProduct([1, 5, 4, 5]))  # 16
print(Solution().maxProduct([3, 7]))  # 12
