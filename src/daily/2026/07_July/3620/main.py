from typing import List
from collections import defaultdict, deque


class Solution:
  def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
    """
    3620. Network Recovery Pathways

    Binary search on the minimum edge cost threshold X. For each X, run a
    topological DP on the DAG using only edges with cost >= X to find the
    minimum total cost path through online nodes. If it's <= k, X is achievable.

    Time: O((n + m) log m)
    Space: O(n + m)
    """
    n = len(online)
    adj = defaultdict(list)
    in_deg = [0] * n
    for u, v, cost in edges:
      adj[u].append((v, cost))
      in_deg[v] += 1

    # Topological order via Kahn's algorithm (computed once)
    topo = []
    q = deque(i for i in range(n) if in_deg[i] == 0)
    temp_deg = in_deg[:]
    while q:
      node = q.popleft()
      topo.append(node)
      for v, _ in adj[node]:
        temp_deg[v] -= 1
        if temp_deg[v] == 0:
          q.append(v)

    unique_costs = sorted(set(c for _, _, c in edges))

    def can_achieve(min_cost):
      dist = [float('inf')] * n
      dist[0] = 0
      for u in topo:
        if dist[u] == float('inf'):
          continue
        if u != 0 and u != n - 1 and not online[u]:
          continue
        for v, cost in adj[u]:
          if cost < min_cost:
            continue
          if v != n - 1 and not online[v]:
            continue
          if dist[u] + cost < dist[v]:
            dist[v] = dist[u] + cost
      return dist[n - 1] <= k

    res = -1
    lo, hi = 0, len(unique_costs) - 1
    while lo <= hi:
      mid = (lo + hi) // 2
      if can_achieve(unique_costs[mid]):
        res = unique_costs[mid]
        lo = mid + 1
      else:
        hi = mid - 1

    return res


print(Solution().findMaxPathScore([[0,1,5],[1,3,10],[0,2,3],[2,3,4]], [True,True,True,True], 10))  # 3
print(Solution().findMaxPathScore([[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], [True,True,True,False,True], 12))  # 6
