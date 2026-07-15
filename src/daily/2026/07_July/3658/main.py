class Solution:
  def gcdOfOddEvenSums(self, n: int) -> int:
    """
    3658. GCD of Odd and Even Sums

    Due to mathematical properties of even numbers sum (2+4+6+...+2n = n(n+1))
    and odd numbers sum (1+3+5+...+(2n-1) = n^2),
    the GCD of these two sums is always equal to n due to gcd(n^2, n(n+1)) = n*gcd(n, n+1) = n.

    Time: O(1)
    Space: O(1)
    """
    return n


print(Solution().gcdOfOddEvenSums(4))  # Output: 4
print(Solution().gcdOfOddEvenSums(5))  # Output: 5
