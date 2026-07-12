from typing import List


class Solution:
  def arrayRankTransform(self, arr: List[int]) -> List[int]:
    """
    1331. Rank Transform of an Array

    Sort the initial array and assign ranks to each unique value. Then, map the original values to their ranks.

    Time: O(n log n)
    Space: O(n)
    """
    rank = {v: i + 1 for i, v in enumerate(sorted(set(arr)))}
    return [rank[v] for v in arr]


print(Solution().arrayRankTransform([40, 10, 20, 30]))  # [4,1,2,3]
print(Solution().arrayRankTransform([100, 100, 100]))  # [1,1,1]
print(Solution().arrayRankTransform(
    [37, 12, 28, 9, 100, 56, 80, 5, 12]))  # [5,3,4,2,8,6,7,1,3]
