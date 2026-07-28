class Solution:
  def smallestPalindrome(self, s: str) -> str:
    """
    3517. Smallest Palindromic Rearrangement I

    Using counting sort, construct the first half of the palindrome (while keeping in mind the middle character).
    Return the concatenation of half, middle char and mirror (half[::-1])

    Time: O(n)
    Space: O(n)
    """
    if len(s) == 1:
      return s

    count_arr = [0] * 256
    middle = ''
    result_arr = []
    for char in s:
      count_arr[ord(char)] += 1
    for i in range(len(count_arr)):
      if count_arr[i] > 0:
        if count_arr[i] % 2 == 1:
          middle = chr(i)
        result_arr.append(chr(i) * (count_arr[i] // 2))

    half = "".join(result_arr)
    return "".join([half, middle, half[::-1]])


print(Solution().smallestPalindrome("z"))  # z
print(Solution().smallestPalindrome("babab"))  # abbba
print(Solution().smallestPalindrome("daccad"))  # acddca
