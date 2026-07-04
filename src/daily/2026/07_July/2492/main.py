from typing import List


class Solution:
  def minScore(self, n: int, roads: List[List[int]]) -> int:
    """
    2492. Minimum Score of a Path Between Two Cities

    DFS to find all nodes reachable from node 1, and return the minimum edge
    cost among those edges.

    Time: O(n + m)
    Space: O(n + m)
    """
    adj = [[] for _ in range(n)]
    for u, v, cost in roads:
      adj[u - 1].append((v - 1, cost))
      adj[v - 1].append((u - 1, cost))

    visited = [False] * n
    min_cost = float('inf')

    def dfs(node):
      nonlocal min_cost
      visited[node] = True
      for neighbor, cost in adj[node]:
        min_cost = min(min_cost, cost)
        if not visited[neighbor]:
          dfs(neighbor)

    dfs(0)
    return min_cost


print(Solution().minScore(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))  # 5
print(Solution().minScore(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]))  # 2
