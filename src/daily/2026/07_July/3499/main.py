class Solution:
  def maxActiveSectionsAfterTrade(self, s: str) -> int:
    """
    3499. Maximize Active Section with Trade I

    Find all contiguous blocks of 0. If there are fewer than 2 blocks of '0's,
    no valid internal trade is possible - return the original number of 1.
    Otherwise, find the maximum sum of any two adjacent 0 blocks separated by a 1 block.
    The answer is the initial count of  plus this maximum sum.

    Time: O(n)
    Space: O(1)
    """
    initial_ones = 0
    prev_zeros = -1
    current_zeros = 0
    max_gain = -1

    for char in s:
      if char == "1":
        initial_ones += 1
        if current_zeros > 0 and prev_zeros != -1:
          gain = prev_zeros + current_zeros
          if gain > max_gain:
            max_gain = gain

          prev_zeros = current_zeros
          current_zeros = 0
      else:
        current_zeros += 1

    if current_zeros > 0 and prev_zeros != -1:
      gain = prev_zeros + current_zeros
      if gain > max_gain:
        max_gain = gain

    if max_gain == -1:
      return initial_ones

    return initial_ones + max_gain
