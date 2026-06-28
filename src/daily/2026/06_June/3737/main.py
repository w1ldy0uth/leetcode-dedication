from collections import defaultdict
from typing import List


class Solution:
  def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
    """
    3737. Count Subarrays With Majority Element I

    Map target to +1, others to -1. A subarray [i+1..j] has target as majority
    iff prefix[j] > prefix[i]. Since prefix changes by ±1 each step, maintain
    a running count of how many previous prefixes are strictly less than the
    current one, updating in O(1) per step using a frequency map.

    Time: O(n).
    Space: O(n).
    """
    freq = defaultdict(int)
    freq[0] = 1
    prefix = 0
    less = 0
    res = 0

    for num in nums:
      old = prefix
      prefix += 1 if num == target else -1
      if prefix > old:
        less += freq[old]
      else:
        less -= freq[prefix]
      res += less
      freq[prefix] += 1

    return res


print(Solution().countMajoritySubarrays([1, 2, 2, 3], 2))  # 5
print(Solution().countMajoritySubarrays([1, 1, 1, 1], 1))  # 10
print(Solution().countMajoritySubarrays([1, 2, 3], 4))      # 0
