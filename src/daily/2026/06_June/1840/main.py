from typing import List


class Solution:
  def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
    """
    1840. Maximum Building Height

    Sort restrictions and add sentinels for building 1 (height 0) and building n.
    Propagate height limits left-to-right then right-to-left so each restriction
    is consistent with its neighbors. Between two consecutive restricted buildings
    at positions p1, p2 with heights h1, h2, the peak is (p2 - p1 + h1 + h2) // 2.

    Time: O(n log n) where n = len(restrictions), dominated by sort.
    Space: O(n).
    """
    r = sorted(restrictions + [[1, 0]])

    for i in range(1, len(r)):
      r[i][1] = min(r[i][1], r[i - 1][1] + r[i][0] - r[i - 1][0])

    for i in range(len(r) - 2, -1, -1):
      r[i][1] = min(r[i][1], r[i + 1][1] + r[i + 1][0] - r[i][0])

    ans = 0
    for i in range(len(r) - 1):
      p1, h1 = r[i]
      p2, h2 = r[i + 1]
      ans = max(ans, (p2 - p1 + h1 + h2) // 2)

    p, h = r[-1]
    ans = max(ans, h + n - p)

    return ans


print(Solution().maxBuilding(5, [[2, 1], [4, 1]]))                     # 2
print(Solution().maxBuilding(6, []))                                   # 5
print(Solution().maxBuilding(10, [[5, 3], [2, 5], [7, 4], [10, 3]]))   # 5
