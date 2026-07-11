from typing import List


class Solution:
  def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
    """
    2685. Count the Number of Complete Components

    Find connected components with Union-Find, tracking node count and edge count
    per component. A component with k nodes is complete if it has k*(k-1)/2 edges.

    Time: O(n + m * α(n))
    Space: O(n)
    """
    parent = list(range(n))
    size = [1] * n
    edge_count = [0] * n

    def find(x: int) -> int:
      while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
      return x

    def union(a: int, b: int) -> None:
      a, b = find(a), find(b)
      if a == b:
        edge_count[a] += 1
        return
      if size[a] < size[b]:
        a, b = b, a
      parent[b] = a
      size[a] += size[b]
      edge_count[a] += edge_count[b] + 1

    for u, v in edges:
      union(u, v)

    return sum(
      1 for i in range(n)
      if find(i) == i and edge_count[i] == size[i] * (size[i] - 1) // 2
    )


print(Solution().countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4]]))        # 3
print(Solution().countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4],[3,5]]))  # 1
