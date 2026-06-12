from collections import deque
from typing import List


class Solution:
  def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    """
    3559. Number of Ways to Assign Edge Weights II

    For a path with k edges, each assigned 1 or 2, the sum is odd iff the number
    of weight-1 edges is odd. By symmetry exactly half of all 2^k assignments
    yield an odd sum, so the answer per query is 2^(k-1) (or 0 if k=0).

    k = depth[u] + depth[v] - 2*depth[LCA(u,v)] is found via binary lifting
    in O(log n) per query after O(n log n) preprocessing.
    """
    MOD = 10 ** 9 + 7
    n = len(edges) + 1
    LOG = max(1, n.bit_length())

    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)

    depth = [0] * (n + 1)
    up = [[0] * (n + 1) for _ in range(LOG)]

    # BFS from root 1 to set depth and direct parent
    visited = bytearray(n + 1)
    visited[1] = 1
    up[0][1] = 1
    q = deque([1])
    while q:
      node = q.popleft()
      for nei in adj[node]:
        if not visited[nei]:
          visited[nei] = 1
          depth[nei] = depth[node] + 1
          up[0][nei] = node
          q.append(nei)

    # Binary lifting table
    for k in range(1, LOG):
      for v in range(1, n + 1):
        up[k][v] = up[k - 1][up[k - 1][v]]

    def lca(u, v):
      if depth[u] < depth[v]:
        u, v = v, u
      diff = depth[u] - depth[v]
      for k in range(LOG):
        if (diff >> k) & 1:
          u = up[k][u]
      if u == v:
        return u
      for k in range(LOG - 1, -1, -1):
        if up[k][u] != up[k][v]:
          u = up[k][u]
          v = up[k][v]
      return up[0][u]

    # Precompute powers of 2 up to n
    pow2 = [1] * (n + 1)
    for i in range(1, n + 1):
      pow2[i] = pow2[i - 1] * 2 % MOD

    result = []
    for u, v in queries:
      l = lca(u, v)
      k = depth[u] + depth[v] - 2 * depth[l]
      result.append(0 if k == 0 else pow2[k - 1])
    return result


print(Solution().assignEdgeWeights([[1, 2]], [[1, 1], [1, 2]])) # [0, 1]
print(Solution().assignEdgeWeights([[1, 2], [1, 3], [3, 4], [3, 5]], [[1, 4], [3, 4], [2, 5]])) # [2, 1, 4]
