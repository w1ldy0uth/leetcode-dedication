from typing import List


class Solution:
  def pathsWithMaxScore(self, board: List[str]) -> List[int]:
    """
    1301. Number of Paths with Max Score

    DP from 'S' (bottom-right) to 'E' (top-left), tracking (max_score, path_count)
    at each cell. Each cell looks at three predecessors (below, right, diagonal)
    and inherits the best score, summing counts on ties.

    Time: O(n^2)
    Space: O(n^2)
    """
    n = len(board)
    MOD = 10**9 + 7
    score = [[-1] * n for _ in range(n)]
    count = [[0] * n for _ in range(n)]

    score[n - 1][n - 1] = 0
    count[n - 1][n - 1] = 1

    for r in range(n - 1, -1, -1):
      for c in range(n - 1, -1, -1):
        if r == n - 1 and c == n - 1:
          continue
        if board[r][c] == 'X':
          continue

        best, cnt = -1, 0
        for dr, dc in [(1, 0), (0, 1), (1, 1)]:
          pr, pc = r + dr, c + dc
          if pr < n and pc < n and score[pr][pc] != -1:
            if score[pr][pc] > best:
              best, cnt = score[pr][pc], count[pr][pc]
            elif score[pr][pc] == best:
              cnt = (cnt + count[pr][pc]) % MOD

        if best == -1:
          continue

        val = 0 if board[r][c] in ('E', 'S') else int(board[r][c])
        score[r][c] = best + val
        count[r][c] = cnt

    if score[0][0] == -1:
      return [0, 0]
    return [score[0][0], count[0][0]]


print(Solution().pathsWithMaxScore(["E23", "2X2", "12S"]))  # [7, 1]
print(Solution().pathsWithMaxScore(["E12", "1X1", "21S"]))  # [4, 2]
print(Solution().pathsWithMaxScore(["E11", "XXX", "11S"]))  # [0, 0]
