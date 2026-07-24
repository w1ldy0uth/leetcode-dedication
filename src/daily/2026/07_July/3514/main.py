from typing import List


class Solution:
  def uniqueXorTriplets(self, nums: List[int]) -> int:
    """
    3514. Number of Unique XOR Triplets II

    Build a frequency array and apply the Fast Walsh–Hadamard Transform, which converts XOR convolution into pointwise multiplication.
    Cube each transformed value, apply the inverse transform, and count the positive entries representing achievable XORs of three elements.

    Time: O(n + m * log m)
    Space: O(m)
    """
    size = 1
    while size <= max(nums):
      size <<= 1

    frequency = [0] * size
    for value in nums:
      frequency[value] += 1

    def fwht(array: List[int]) -> None:
      length = 1

      while length < len(array):
        for start in range(0, len(array), length * 2):
          for i in range(start, start + length):
            left = array[i]
            right = array[i + length]

            array[i] = left + right
            array[i + length] = left - right

        length <<= 1

    # Transform.
    fwht(frequency)

    # Three-way XOR convolution.
    for i in range(size):
      frequency[i] **= 3

    # The inverse FWHT is the same transform followed by division by size.
    fwht(frequency)

    for i in range(size):
      frequency[i] //= size

    return sum(count > 0 for count in frequency)


print(Solution().uniqueXorTriplets([1, 3]))  # 2
print(Solution().uniqueXorTriplets([6, 7, 8, 9]))  # 4
