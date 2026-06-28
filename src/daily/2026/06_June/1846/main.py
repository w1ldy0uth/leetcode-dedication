from typing import List


class Solution:
  def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
    """
    1846. Maximum Element After Decreasing and Rearranging

    Sort the array, then greedily set each element to min(arr[i], arr[i-1] + 1).
    The answer is the last element.

    Time: O(n log n)
    Space: O(1)
    """
    arr.sort()
    arr[0] = 1
    for i in range(1, len(arr)):
      arr[i] = min(arr[i], arr[i - 1] + 1)
    return arr[-1]


print(Solution().maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]))  # 2
print(Solution().maximumElementAfterDecrementingAndRearranging([100, 1, 1000]))  # 3
print(Solution().maximumElementAfterDecrementingAndRearranging([1, 2, 3, 4, 5]))  # 5
