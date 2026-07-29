from collections import Counter
from math import comb


class Solution:
  def smallestPalindrome(self, s: str, k: int) -> str:
    """
    3518. Smallest Palindromic Rearrangement II

    Reduce the problem to finding the k-th lexicographic distinct permutation of the palindrome's left half.
    Use multinomial counts to determine how many permutations begin with each possible character,
    skip entire groups until locating the group containing k, then mirror the selected half around the optional middle character.

    Time: O(n * |∑|)
    Space: O(n * |∑|)
    """
    frequency = Counter(s)

    half = [frequency[chr(ord("a") + i)] // 2 for i in range(26)]
    middle = next(
        (
            chr(ord("a") + i)
            for i in range(26)
            if frequency[chr(ord("a") + i)] % 2
        ),
        "",
    )

    remaining = len(s) // 2

    ways = 1
    available = remaining

    for count in half:
      ways *= comb(available, count)
      available -= count

    if k > ways:
      return ""

    left = []

    while remaining:
      for i in range(26):
        count = half[i]
        if count == 0:
          continue

        block_size = ways * count // remaining

        if k > block_size:
          k -= block_size
          continue

        left.append(chr(ord("a") + i))
        half[i] -= 1
        remaining -= 1
        ways = block_size
        break

    left = "".join(left)
    return left + middle + left[::-1]


print(Solution().smallestPalindrome("abba", 2)) # "baab"
print(Solution().smallestPalindrome("aa", 2)) # ""
print(Solution().smallestPalindrome("bacab", 2)) # "abcba"