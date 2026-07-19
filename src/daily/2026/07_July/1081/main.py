class Solution:
  def smallestSubsequence(self, s: str) -> str:
    """
    1081. Smallest Subsequence of Distinct Characters

    By using monotonic stack, remove larger characters from the end if they appear again later.
    This produces the smallest lexicographic result without losing any distinct character.

    Time: O(n)
    Space: O(1)
    """
    last = {char: i for i, char in enumerate(s)}
    stack = []
    used = set()

    for i, char in enumerate(s):
      if char in used:
        continue

      while (stack and stack[-1] > char and last[stack[-1]] > i):
        used.remove(stack.pop())

      stack.append(char)
      used.add(char)

    return "".join(stack)


print(Solution().smallestSubsequence("bcabc"))  # "abc"
print(Solution().smallestSubsequence("cbacdcbc"))  # "acdb"
