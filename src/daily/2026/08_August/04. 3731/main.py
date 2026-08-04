from typing import List


class Solution:
  def findMissingElements(self, nums: List[int]) -> List[int]:
    """
    3731. Find Missing Elements

    Simply convert an input array to a set to reduce the lookup time from O(n) to O(1).
    Then, iterate through the range of the minimum and maximum values in the input array, checking for missing elements.

    Time: O(n + m)
    Space: O(n)
    """

    if not nums:
      return []

    # Convert list to a set for O(1) lookups
    num_set = set(nums)

    max_val, min_val = max(nums), min(nums)
    res = []

    for i in range(min_val, max_val + 1):
      # This lookup is now O(1) instead of O(n)
      if i not in num_set:
        res.append(i)

    return res


print(Solution().findMissingElements([1, 4, 2, 5]))  # Output: [3]
print(Solution().findMissingElements([7, 8, 6, 9]))  # Output: []
print(Solution().findMissingElements([5, 1]))  # Output: [2, 3, 4]
