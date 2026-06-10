import heapq
from typing import List


class Solution:
  def maxTotalValue(self, nums: List[int], k: int) -> int:
    """
    3691. Maximum Total Subarray Value II

    We need the k highest-value distinct subarrays. Build a sparse table for
    O(1) RMQ, then use a greedy max-heap seeded with [l, n-1] for every l.
    Each time we pop [l, r], we push [l, r-1]: this lazily traverses all
    n*(n+1)/2 subarrays in decreasing-value order without materializing them.
    """
    n = len(nums)
    LOG = n.bit_length() + 1

    # Sparse table for range max and min
    mx = [nums[:]]
    mn = [nums[:]]
    for j in range(1, LOG):
      half = 1 << (j - 1)
      prev_mx = mx[j - 1]
      prev_mn = mn[j - 1]
      row_mx = [max(prev_mx[i], prev_mx[i + half]) for i in range(n - (1 << j) + 1)]
      row_mn = [min(prev_mn[i], prev_mn[i + half]) for i in range(n - (1 << j) + 1)]
      mx.append(row_mx)
      mn.append(row_mn)

    def val(l: int, r: int) -> int:
      length = r - l + 1
      p = length.bit_length() - 1
      rr = r - (1 << p) + 1
      return max(mx[p][l], mx[p][rr]) - min(mn[p][l], mn[p][rr])

    # Seed heap with all subarrays ending at n-1
    heap: list = []
    for l in range(n):
      heapq.heappush(heap, (-val(l, n - 1), l, n - 1))

    total = 0
    for _ in range(k):
      neg_v, l, r = heapq.heappop(heap)
      total -= neg_v
      if r - 1 >= l:
        heapq.heappush(heap, (-val(l, r - 1), l, r - 1))

    return total


print(Solution().maxTotalValue([1, 3, 2], 2))     # 4
print(Solution().maxTotalValue([4, 2, 5, 1], 3))  # 12
print(Solution().maxTotalValue([5], 1))            # 0
