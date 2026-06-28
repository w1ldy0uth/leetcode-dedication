class Solution:
  def maxNumberOfBalloons(self, text: str) -> int:
    """
    1189. Maximum Number of Balloons
    
    Count each unique "balloon" character form an input (normalizing "l" and "o")
    and return a minimal value
    
    Time: O(n)
    Space: O(n)
    """
    balloon_counts = {
      "b": text.count("b"),
      "a": text.count("a"),
      "l": text.count("l") // 2,
      "o": text.count("o") // 2,
      "n": text.count("n")
    }
    
    return min(balloon_counts.values())


print(Solution().maxNumberOfBalloons("nlaebolko")) # 1
print(Solution().maxNumberOfBalloons("loonbalxballpoon")) # 2
print(Solution().maxNumberOfBalloons("leetcode")) # 0
print(Solution().maxNumberOfBalloons("nllbblooon")) # 0
