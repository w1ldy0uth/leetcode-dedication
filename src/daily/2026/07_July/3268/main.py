from typing import List
from collections import deque


class Solution:
  def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
    """
    3268.Find a Safe Walk Through a Grid

    We walk through a grid using 0-1 BFS with tracking the minimum damage.

    Time: O(m * n)
    Space: O(m * n)
    """
    m, n = len(grid), len(grid[0])
    damage = [[float('inf')] * n for _ in range(m)]
    damage[0][0] = grid[0][0]

    dq = deque([(0, 0)])
    while dq:
      r, c = dq.popleft()
      for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < m and 0 <= nc < n:
          cost = damage[r][c] + grid[nr][nc]
          if cost < damage[nr][nc]:
            damage[nr][nc] = cost
            if grid[nr][nc] == 0:
              dq.appendleft((nr, nc))
            else:
              dq.append((nr, nc))

    return health > damage[m - 1][n - 1]


print(Solution().findSafeWalk(
    [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 1))  # True
print(Solution().findSafeWalk([[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [
      0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0]], 3))  # False
print(Solution().findSafeWalk([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 5))  # True
