class Solution:
  def sumAndMultiply(self, n: int) -> int:
    """
    3754. Concatenate Non-Zero Digits and Multiply by Sum I

    Get the last digit by taking n % 10. If it's non-zero, add it to the concatenated number and add it to the sum.
    Then, divide n by 10 to remove the last digit and repeat until n is 0.

    Time: O(log n)
    Space: O(1)
    """
    x, sum = 0, 0
    mult = 1
    while n > 0:
      digit = n % 10

      if digit != 0:
        x += digit * mult
        sum += digit
        mult *= 10

      n //= 10
    return x * sum


print(Solution().sumAndMultiply(10203004))  # Output: 12340
print(Solution().sumAndMultiply(1000))  # Output: 1
