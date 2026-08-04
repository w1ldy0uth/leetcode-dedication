class Solution:
  def longestValidParentheses(self, s: str) -> int:
    """
    32. Longest Valid Parentheses

    Keep a stack of indices of unmatched characters. Seed it with -1 as a sentinel base.
    When a `)` matches, the current valid run's length is `i - stack[-1]`,
    where `stack[-1]` is either the last unmatched `(` position or that base marker.

    Time: O(n)
    Space: O(n)
    """
    stack = [-1]
    best = 0

    for i, ch in enumerate(s):
      if ch == '(':
        stack.append(i)
      else:
        stack.pop()
        if not stack:
          stack.append(i)
        else:
          best = max(best, i - stack[-1])

    return best


print(Solution().longestValidParentheses("(()"))  # Output: 2
print(Solution().longestValidParentheses(")()())"))  # Output: 4
print(Solution().longestValidParentheses(""))  # Output: 0
