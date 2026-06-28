from functools import lru_cache


class Solution:
  def totalWaviness(self, num1: int, num2: int) -> int:
    """
    3751. Total Waviness of Numbers in Range I (also suitable for 3752. Total Waviness of Numbers in Range II)

    Digit DP prefix sum: f(num2) - f(num1-1), where f(N) = total waviness of [1, N].
    We place digits left to right; when placing d at pos, we score prev1 as peak/valley
    using prev2 (left neighbor) and d (right neighbor). First and last digits are excluded
    naturally — first has no prev2, last is never followed by a scoring step.

    States: pos × prev2 × prev1 × tight × started → O(d * 11 * 11 * 2 * 2) per query.
    """
    def count_up_to(N: int) -> int:
      if N <= 0:
        return 0
      digits = list(map(int, str(N)))
      n = len(digits)

      @lru_cache(maxsize=None)
      def count(pos, tight):
        """Count of valid completions from pos, assuming a real digit has been started."""
        if pos == n:
          return 1
        limit = digits[pos] if tight else 9
        return sum(count(pos + 1, tight and d == limit) for d in range(limit + 1))

      @lru_cache(maxsize=None)
      def dp(pos, prev2, prev1, tight, started):
        if pos == n:
          return 0

        limit = digits[pos] if tight else 9
        total = 0

        for d in range(limit + 1):
          new_tight = tight and d == limit

          if not started:
            if d == 0:
              total += dp(pos + 1, -1, -1, new_tight, False)
            else:
              total += dp(pos + 1, -1, d, new_tight, True)
          else:
            score = 0
            if prev2 != -1 and (
              prev1 > prev2 and prev1 > d or
              prev1 < prev2 and prev1 < d
            ):
              score = 1
            # score applies to every valid completion from pos+1 onwards
            total += score * count(pos + 1, new_tight) + dp(pos + 1, prev1, d, new_tight, True)

        return total

      result = dp(0, -1, -1, True, False)
      dp.cache_clear()
      count.cache_clear()
      return result

    return count_up_to(num2) - count_up_to(num1 - 1)


print(Solution().totalWaviness(120, 130))   # 3
print(Solution().totalWaviness(198, 202))   # 3
print(Solution().totalWaviness(4848, 4848)) # 2
