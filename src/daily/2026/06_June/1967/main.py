from typing import List


class Solution:
  def numOfStrings(self, patterns: List[str], word: str) -> int:
    """
    1967. Number of Strings That Appear as Substrings in Word
    
    Simply iterate through the patterns and check if each pattern is a substring of the word using the 'in' operator.
    
    Time: O(n * m * k) where n is the number of patterns, m is the length of the word and k is the average length of the patterns.
    Space: O(1)
    """
    count = 0
    for pattern in patterns:
      if pattern in word:
        count += 1
    return count


print(Solution().numOfStrings(["a", "abc", "bc", "d"], "abc"))  # 3
print(Solution().numOfStrings(["a", "b", "c"], "aaaaabbbbb"))  # 2
print(Solution().numOfStrings(["a", "a", "a"], "ab"))  # 3
