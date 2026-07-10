import bisect
from typing import List


class Solution:
  def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
    """
    3534. Path Existence Queries in a Graph II

    Sort nodes by value. In sorted order, each node p can reach a contiguous
    window [L[p], R[p]] in one hop. To minimize hops from pu to pv (pu <= pv),
    greedily jump to R[p] each time — optimal since R is non-decreasing in sorted
    order. Use binary lifting on R for O(log n) per query.

    Time: O((n + q) log n)
    Space: O(n log n)
    """
    order = sorted(range(n), key=lambda i: nums[i])
    rank = [0] * n
    for p, node in enumerate(order):
      rank[node] = p

    sv = [nums[order[p]] for p in range(n)]  # sorted values

    # R[p] = rightmost sorted position reachable from p in one hop
    R = [bisect.bisect_right(sv, sv[p] + maxDiff) - 1 for p in range(n)]

    # Binary lifting: anc[k][p] = sorted position reached after 2^k greedy jumps from p
    LOG = 17
    anc = [R[:]]
    for k in range(1, LOG):
      prev = anc[k - 1]
      anc.append([prev[prev[p]] for p in range(n)])

    def min_dist(pu: int, pv: int) -> int:
      if pu == pv:
        return 0
      if pu > pv:
        pu, pv = pv, pu
      if R[pu] >= pv:
        return 1
      cur, dist = pu, 0
      for k in range(LOG - 1, -1, -1):
        if anc[k][cur] < pv:
          cur = anc[k][cur]
          dist += 1 << k
      cur = anc[0][cur]
      dist += 1
      return dist if cur >= pv else -1

    return [min_dist(rank[u], rank[v]) for u, v in queries]


print(Solution().pathExistenceQueries(5, [1, 8, 3, 4, 2], 3, [[0, 3], [2, 4]]))               # [1, 1]
print(Solution().pathExistenceQueries(5, [5, 3, 1, 9, 10], 2, [[0, 1], [0, 2], [2, 3], [4, 3]]))  # [1, 2, -1, 1]
print(Solution().pathExistenceQueries(3, [3, 6, 1], 1, [[0, 0], [0, 1], [1, 2]]))             # [0, -1, -1]
