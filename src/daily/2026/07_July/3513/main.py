class Solution:
  def uniqueXorTriplets(self, nums: List[int]) -> int:
    """
    3513. Number of Unique XOR Triplets I

    Mathematical observation that unique XOR triplets cover all values up to the next power of two.

    Time: O(1)
    Space: O(1)
    """
    n = len(nums)

    if n <= 2:
      return n

    return 1 << n.bit_length()


print(Solution().uniqueXorTriplets([1,2])) # 2
print(Solution().uniqueXorTriplets([3,1,2])) # 4
