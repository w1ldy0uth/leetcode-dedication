class Solution:
  def maxProduct(self, n: int) -> int:
    """
    3536. Maximum Product of Two Digits

    Find the two largest digits in a single pass using divmod 10.

    Time: O(d)
    Space O(1)
    """
    first = second = 0
    while n:
      n, d = divmod(n, 10)
      if d > first:
        first, second = d, first
      elif d > second:
        second = d
    return first * second


print(Solution().maxProduct(31))  # 3
print(Solution().maxProduct(22))  # 4
print(Solution().maxProduct(124))  # 8
