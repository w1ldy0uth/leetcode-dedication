from typing import List


class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    """
    22. Generate Parentheses

    Keep track of the number of left and right parentheses used so far.
    We can add a left parenthesis if we haven't used all of them yet,
    and we can add a right parenthesis if it won't lead to an invalid sequence.

    Time: O(4^n / sqrt(n)) - Catalan number C_n
    Space: O(n)
    """
    def backtrack(s: str, left: int, right: int):
      if len(s) == 2 * n:
        res.append(s)
        return
      if left < n:
        backtrack(s + '(', left + 1, right)
      if right < left:
        backtrack(s + ')', left, right + 1)

    res = []
    backtrack('', 0, 0)
    return res

print(Solution().generateParenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
print(Solution().generateParenthesis(1))  # Output: ["()"]
