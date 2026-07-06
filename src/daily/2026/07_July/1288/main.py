from typing import List


class Solution:
  def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    """
    1288. Remove Covered Intervals

    Sort intervals by start ascending, end descending. Then iterate through
    intervals, keeping track of the maximum end seen so far. If the current
    interval's end is less than or equal to the max end, it is covered.

    Time: O(n log n)
    Space: O(1)
    """
    intervals.sort(key=lambda x: (x[0], -x[1]))
    count = 0
    max_end = 0

    for start, end in intervals:
      if end <= max_end:
        count += 1
      else:
        max_end = end

    return len(intervals) - count


print(Solution().removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))  # Output: 2
print(Solution().removeCoveredIntervals([[1, 4], [2, 3]]))  # Output: 1
