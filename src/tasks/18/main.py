from typing import List


class Solution:
  def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    """
    18. 4Sum
    
    Iterate through the each pair and find another suitable pair using two pointers
    while skipping duplicates and using early termination to reduce the search space.
    
    Time: O(n^3) — three nested loops, two pointers in the innermost loop.
    Space: O(1)
    """
    res = []
    nums.sort()
    n = len(nums)

    for i in range(n - 3):
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
        break
      if nums[i] + nums[-3] + nums[-2] + nums[-1] < target:
        continue

      for j in range(i + 1, n - 2):
        if j > i + 1 and nums[j] == nums[j - 1]:
          continue
        if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
          break
        if nums[i] + nums[j] + nums[-2] + nums[-1] < target:
          continue

        lo, hi = j + 1, n - 1
        while lo < hi:
          s = nums[i] + nums[j] + nums[lo] + nums[hi]
          if s == target:
            res.append([nums[i], nums[j], nums[lo], nums[hi]])
            while lo < hi and nums[lo] == nums[lo + 1]:
              lo += 1
            while lo < hi and nums[hi] == nums[hi - 1]:
              hi -= 1
            lo += 1
            hi -= 1
          elif s < target:
            lo += 1
          else:
            hi -= 1

    return res


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0)) # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(Solution().fourSum([2, 2, 2, 2, 2], 8))  # [[2,2,2,2]]
