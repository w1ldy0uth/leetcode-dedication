from bisect import bisect_left, bisect_right
from typing import List


class Solution:
  def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
    """
    3501. Maximize Active Section with Trade II

    Represent the string as runs and note that trading a pattern 0^A * 1^B * 0^C increases the total number of ones by A+C.
    For each query, binary search the eligible internal one-runs, evaluate the boundary-clipped candidates directly,
    and use a segment tree to find the maximum full gain among the remaining runs.

    Time: O(n + q * log n)
    Space: O(n)
    """
    n = len(s)
    initial_ones = s.count("1")

    # Build maximal runs: (character, left, right), both endpoints inclusive.
    runs = []
    i = 0

    while i < n:
      j = i
      while j + 1 < n and s[j + 1] == s[i]:
        j += 1

      runs.append((s[i], i, j))
      i = j + 1

    # Information about every 1-run surrounded globally by zero-runs.
    starts = []
    ends = []
    left_zero_start = []
    right_zero_end = []
    full_gain = []

    for i in range(1, len(runs) - 1):
      char, one_left, one_right = runs[i]

      if (
          char == "1"
          and runs[i - 1][0] == "0"
          and runs[i + 1][0] == "0"
      ):
        zero_left = runs[i - 1][1]
        zero_right = runs[i + 1][2]

        starts.append(one_left)
        ends.append(one_right)
        left_zero_start.append(zero_left)
        right_zero_end.append(zero_right)

        full_gain.append(
            (one_left - zero_left) +
            (zero_right - one_right)
        )

    m = len(full_gain)

    # Iterative segment tree for range maximum over full gains.
    size = 1
    while size < m:
      size *= 2

    tree = [0] * (2 * size)

    for i, value in enumerate(full_gain):
      tree[size + i] = value

    for i in range(size - 1, 0, -1):
      tree[i] = max(tree[2 * i], tree[2 * i + 1])

    def range_max(left: int, right: int) -> int:
      """Maximum on the half-open index range [left, right)."""
      result = 0
      left += size
      right += size

      while left < right:
        if left & 1:
          result = max(result, tree[left])
          left += 1

        if right & 1:
          right -= 1
          result = max(result, tree[right])

        left //= 2
        right //= 2

      return result

    def clipped_gain(index: int, query_left: int, query_right: int) -> int:
      one_left = starts[index]
      one_right = ends[index]

      left_part = one_left - max(
          left_zero_start[index],
          query_left
      )
      right_part = min(
          right_zero_end[index],
          query_right
      ) - one_right

      return left_part + right_part

    answer = []

    for query_left, query_right in queries:
      # The one-run must be strictly inside the query. Otherwise it
      # touches an augmented '1' and cannot be surrounded by zeros.
      first = bisect_right(starts, query_left)
      last = bisect_left(ends, query_right) - 1

      if first > last:
        answer.append(initial_ones)
        continue

      best_gain = clipped_gain(first, query_left, query_right)

      if first != last:
        best_gain = max(
            best_gain,
            clipped_gain(last, query_left, query_right)
        )

      # Only the first and last candidates can have zero-runs clipped
      # by query boundaries. Every candidate between them has its full
      # adjacent zero-runs inside the query.
      if first + 1 < last:
        best_gain = max(
            best_gain,
            range_max(first + 1, last)
        )

      answer.append(initial_ones + best_gain)

    return answer


print(Solution().maxActiveSectionsAfterTrade("01", [[0, 1]]))      # [1]
print(Solution().maxActiveSectionsAfterTrade(
    "0100", [[0, 3], [0, 2], [1, 3], [2, 3]]))                     # [4,3,1,1]
print(Solution().maxActiveSectionsAfterTrade(
    "1000100", [[1, 5], [0, 6], [0, 4]]))                          # [6,7,2]
print(Solution().maxActiveSectionsAfterTrade(
    "01010", [[0, 3], [1, 4], [1, 3]]))                            # [4,4,2]
