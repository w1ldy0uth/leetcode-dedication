class Solution:
  def numberOfSubstrings(self, s: str) -> int:
    """
    1358. Number of Substrings Containing All Three Characters

    For each position i, track the last seen index of a, b, and c. The earliest of those three is the leftmost starting point where a valid substring can begin and still end at i.

    Time: O(n)
    Space: O(1)
    """
    last = {'a': -1, 'b': -1, 'c': -1}
    res = 0

    for i, ch in enumerate(s):
      last[ch] = i
      res += min(last.values()) + 1

    return res


print(Solution().numberOfSubstrings("abcabc"))  # 10
print(Solution().numberOfSubstrings("aaacb"))   # 3
print(Solution().numberOfSubstrings("abc"))     # 1
