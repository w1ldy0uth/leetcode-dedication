from collections import deque
from typing import List


class Solution:
  def assignEdgeWeights(self, edges: List[List[int]]) -> int:
    """
    3558. Number of Ways to Assign Edge Weights I

    Only the edges on the path from root to a max-depth node x are assigned.
    For d edges (d = max depth), count assignments of {1,2} with odd sum.
    Sum is odd iff the number of weight-1 edges is odd: 2^(d-1) solutions.
    """
    adj = [[] for _ in range(len(edges) + 2)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    max_depth = 0
    q = deque([(1, 0, 0)])  # node, parent, depth
    while q:
      node, parent, depth = q.popleft()
      max_depth = max(max_depth, depth)
      for nei in adj[node]:
        if nei != parent:
          q.append((nei, node, depth + 1))

    return pow(2, max_depth - 1, 10 ** 9 + 7)


print(Solution().assignEdgeWeights([[1, 2]]))                         # 1
print(Solution().assignEdgeWeights([[1, 2], [1, 3], [3, 4], [3, 5]]))  # 2
print(Solution().assignEdgeWeights([[4, 5], [1, 4], [2, 3], [1, 2]]))  # 2
