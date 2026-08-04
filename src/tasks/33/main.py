from typing import List


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    """
    33. Search in Rotated Sorted Array

    Use binary search to find the target in a rotated sorted array.
    At each step, determine which half of the array is properly sorted,
    and check if the target lies within that range.

    Time: O(log n)
    Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
        return mid
      if nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
          right = mid - 1
        else:
          left = mid + 1
      else:
        if nums[mid] < target <= nums[right]:
          left = mid + 1
        else:
          right = mid - 1

    return -1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))  # Output: -1
print(Solution().search([1], 0))  # Output: -1
