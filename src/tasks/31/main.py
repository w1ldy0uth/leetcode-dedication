from typing import List


class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    """
    31. Next Permutation

    Use single-pass peak-and-valley approach to find the next permutation in place.
    If the array sorted in descending order, the algorithm reverses it to get the smallest permutation.

    Time: O(n)
    Space: O(1)
    """
    n = len(nums)
    i = n - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
      i -= 1

    if i >= 0:
      j = n - 1
      while nums[j] <= nums[i]:
        j -= 1
      nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1:] = reversed(nums[i + 1:])
    print(nums)


Solution().nextPermutation([1, 2, 3])  # [1, 3, 2]
Solution().nextPermutation([3, 2, 1])  # [1, 2, 3]
Solution().nextPermutation([1, 1, 5])  # [1, 5, 1]
