class Solution:
  def minimumPushes(self, word: str) -> int:
    """
    3014. Minimum Number of Pushes to Type Word I

    Assign most frequent letters to lowest cost positions using greedy strategy.

    Time: O(n)
    Space: O(1)
    """
    return sum(i // 8 + 1 for i in range(len(word)))


print(Solution().minimumPushes("abcde")) # 5
print(Solution().minimumPushes("xycdefghij")) # 12
