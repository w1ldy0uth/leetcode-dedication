from typing import List


class Solution:
  def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
    """
    2812. Find the Safest Path in a Grid

    First, we get the safeness factor of each cell by performing a multi-source BFS from all thieves.
    Then, we perform a binary search on the safeness factor k and check if there exists a path from (0, 0) to (n - 1, n - 1)
    such that all cells in the path have a safeness factor >= k.

    Time: O(n^2 log(n)) where n is the size of the grid.
    Space: O(n^2)
    """
    from collections import deque

    n = len(grid)
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Step 1: multi-source BFS from all thieves
    dist = [[float('inf')] * n for _ in range(n)]
    queue = deque()
    for r in range(n):
      for c in range(n):
        if grid[r][c] == 1:
          dist[r][c] = 0
          queue.append((r, c))

    while queue:
      r, c = queue.popleft()
      for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
          dist[nr][nc] = dist[r][c] + 1
          queue.append((nr, nc))

    # Step 2: binary search on safeness value k
    def can_reach(k: int) -> bool:
      if dist[0][0] < k or dist[n - 1][n - 1] < k:
        return False
      seen = [[False] * n for _ in range(n)]
      seen[0][0] = True
      q = deque([(0, 0)])
      while q:
        r, c = q.popleft()
        if r == n - 1 and c == n - 1:
          return True
        for dr, dc in DIRS:
          nr, nc = r + dr, c + dc
          if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc] and dist[nr][nc] >= k:
            seen[nr][nc] = True
            q.append((nr, nc))
      return False

    lo, hi, ans = 0, n * 2, 0
    while lo <= hi:
      mid = (lo + hi) // 2
      if can_reach(mid):
        ans = mid
        lo = mid + 1
      else:
        hi = mid - 1

    return ans


print(Solution().maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))  # 0
