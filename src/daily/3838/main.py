from typing import List


class Solution:
  def wordMapping(self, words: List[str], weights: List[int]) -> str:
    """
    3838. Weighted Word Mapping

    Sum the character weights for each word, take mod 26, then map to a letter
    using reverse alphabetical order (0 → 'z', 1 → 'y', ..., 25 → 'a').
    """
    return ''.join(
      chr(ord('z') - (sum(weights[ord(c) - ord('a')] for c in word) % 26))
      for word in words
    )


print(Solution().wordMapping(
  ["abcd", "def", "xyz"],
  [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]
))  # "rij"
print(Solution().wordMapping(
  ["a", "b", "c"],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
))  # "yyy"
print(Solution().wordMapping(
  ["abcd"],
  [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]
))  # "g"
