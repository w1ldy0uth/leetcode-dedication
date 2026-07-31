from collections import Counter


class Solution:
  def minimumPushes(self, word: str) -> int:
    """
    3016. Minimum Number of Pushes to Type Word II

    Count each letter’s frequency and assign the most frequent letters to the cheapest keypad positions:
    eight letters cost one push, the next eight cost two, and so on.

    Time: O(n * log n) in general case, for English letters it comes down to O(1)
    Space: O(1)
    """
    frequencies = sorted(Counter(word).values(), reverse=True)

    return sum(frequency * (i // 8 + 1) for i, frequency in enumerate(frequencies))


print(Solution().minimumPushes("abcde"))  # 5
print(Solution().minimumPushes("xyzxyzxyzxyz"))  # 12
print(Solution().minimumPushes("aabbccddeeffgghhiiiiii"))  # 24
