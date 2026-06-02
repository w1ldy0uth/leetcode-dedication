import bisect
from typing import List


def earliest_finish_time(
  landStartTime: List[int],
  landDuration: List[int],
  waterStartTime: List[int],
  waterDuration: List[int],
) -> int:
  """
  3633. Earliest Finish Time for Land and Water Rides I
  
  For each land ride we binary search precomputed prefix/suffix mins over water rides to find
  the best pairing in O(log m) instead of scanning all water rides.
  """
  water_by_ws = sorted(zip(waterStartTime, waterDuration))
  ws_arr = [ws for ws, _ in water_by_ws]

  water_by_W = sorted((ws + wd, wd) for ws, wd in zip(waterStartTime, waterDuration))
  W_arr = [W for W, _ in water_by_W]

  m = len(ws_arr)

  # prefix_min_wd[i] = min wd among water_by_ws[:i]
  prefix_min_wd = [float('inf')] * (m + 1)
  for i, (_, wd) in enumerate(water_by_ws):
    prefix_min_wd[i + 1] = min(prefix_min_wd[i], wd)

  # suffix_min_W_ws[i] = min W among water_by_ws[i:]
  suffix_min_W_ws = [float('inf')] * (m + 1)
  for i in range(m - 1, -1, -1):
    ws, wd = water_by_ws[i]
    suffix_min_W_ws[i] = min(suffix_min_W_ws[i + 1], ws + wd)

  # suffix_min_W[i] = min W among water_by_W[i:]
  suffix_min_W = [float('inf')] * (m + 1)
  for i in range(m - 1, -1, -1):
    suffix_min_W[i] = min(suffix_min_W[i + 1], W_arr[i])

  ans = float('inf')
  for ls, ld in zip(landStartTime, landDuration):
    L = ls + ld

    # Water first with W <= ls → finish = L (best possible for this land ride)
    if bisect.bisect_right(W_arr, ls) > 0:
      ans = min(ans, L)
      continue

    k = bisect.bisect_right(ws_arr, L)

    # Land first, ws <= L → finish = L + min(wd)
    if k > 0:
      ans = min(ans, L + prefix_min_wd[k])

    # Land first, ws > L → finish = min(W)
    if k < m:
      ans = min(ans, suffix_min_W_ws[k])

    # Water first, W > ls (guaranteed since case 1 didn't fire) → finish = min(W) + ld
    ans = min(ans, suffix_min_W[0] + ld)

  return ans


print(earliest_finish_time(
  landStartTime = [2, 8],
  landDuration = [4, 1],
  waterStartTime = [6],
  waterDuration = [3],
))  # 9

print(earliest_finish_time(
  landStartTime = [5],
  landDuration = [3],
  waterStartTime = [1],
  waterDuration = [10],
))  # 14