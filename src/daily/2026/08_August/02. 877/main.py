from typing import List


class Solution:
  def stoneGame(self, piles: List[int]) -> bool:
    """
    877. Stone Game

    Alice can always choose to take only even-indexed piles (or always odd),
    whichever sum is bigger, since the ends alternate parity as the game shrinks.
    So for this exact problem, the answer is always true.

    Time: O(1)
    Space: O(1)
    """
    return True


print(Solution().stoneGame([5, 3, 4, 5]))  # True
print(Solution().stoneGame([3, 7, 2, 3]))  # True
