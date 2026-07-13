from typing import List


class Solution:
  def sequentialDigits(self, low: int, high: int) -> List[int]:
    """
    1291. Sequential Digits

    Every sequential digit number is a contiguous substring of "123456789".
    Generate all such substrings (length 2..9), convert to int, filter by [low, high].
    Iterating by length first guarantees sorted order.

    Time: O(1) — at most 36 candidates regardless of input
    Space: O(1)
    """
    digits = "123456789"
    result = []
    for length in range(2, 10):
      for start in range(9 - length + 1):
        num = int(digits[start:start + length])
        if low <= num <= high:
          result.append(num)
    return result


print(Solution().sequentialDigits(100, 300))    # [123, 234]
print(Solution().sequentialDigits(1000, 13000)) # [1234, 2345, 3456, 4567, 5678, 6789, 12345]
