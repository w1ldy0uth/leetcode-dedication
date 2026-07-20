from typing import List

from numpy import size


class Solution:
  def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    """
    1260. Shift 2D Grid

    Flatten 2D grid to 1D index, apply modular arithmetic for cyclic shift, then map back to 2D.

    Time: O(n * m)
    Space: O(n * m)
    """
    rows, cols = len(grid), len(grid[0])
    size = rows * cols
    k %= size

    result = [[0] * cols for _ in range(rows)]

    for index in range(size):
      old_r, old_c = divmod(index, cols)
      new_r, new_c = divmod((index + k) % size, cols)
      result[new_r][new_c] = grid[old_r][old_c]

    return result


print(Solution().shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
print(Solution().shiftGrid(
    [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4))
