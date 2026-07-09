from typing import List


class Solution:
  def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
    """
    3532. Path Existence Queries in a Graph I

    Since nums is sorted, edges only exist between consecutive nodes (any non-consecutive
    pair with a gap > maxDiff is already blocked by the intermediate nodes). A break
    between consecutive nodes splits the graph into separate components.

    Scan once to assign each node a component ID, then each query is O(1).

    Time: O(n + q)
    Space: O(n)
    """
    comp = [0] * n
    for i in range(1, n):
      comp[i] = comp[i - 1] + (1 if nums[i] - nums[i - 1] > maxDiff else 0)

    return [comp[u] == comp[v] for u, v in queries]


print(Solution().pathExistenceQueries(2, [1, 3], 1, [[0, 0], [0, 1]]))             # [True, False]
print(Solution().pathExistenceQueries(4, [2, 5, 6, 8], 2, [[0, 1], [0, 2], [1, 3], [2, 3]]))  # [False, False, True, True]
