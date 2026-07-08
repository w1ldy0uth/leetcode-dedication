from typing import List


class Solution:
  def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
    """
    3756. Concatenate Non-Zero Digits and Multiply by Sum II

    Precompute three prefix arrays over s (O(n)), then answer each query in O(1):
      - prefix_x[i]:   non-zero digits of s[0..i-1] concatenated as a number (mod MOD)
      - prefix_nz[i]:  count of non-zero digits in s[0..i-1]
      - prefix_sum[i]: sum of non-zero digits in s[0..i-1]

    For query [l, r] with k = count of non-zero digits in that range:
      x[l..r] = prefix_x[r+1] - prefix_x[l] * 10^k  (mod MOD)
      digit_sum = prefix_sum[r+1] - prefix_sum[l]

    Time: O(n + q)
    Space: O(n)
    """
    MOD = 10**9 + 7
    n = len(s)

    prefix_x = [0] * (n + 1)
    prefix_nz = [0] * (n + 1)
    prefix_sum = [0] * (n + 1)

    for i, ch in enumerate(s):
      d = ord(ch) - 48
      if d != 0:
        prefix_x[i + 1] = (prefix_x[i] * 10 + d) % MOD
        prefix_nz[i + 1] = prefix_nz[i] + 1
        prefix_sum[i + 1] = prefix_sum[i] + d
      else:
        prefix_x[i + 1] = prefix_x[i]
        prefix_nz[i + 1] = prefix_nz[i]
        prefix_sum[i + 1] = prefix_sum[i]

    results = []
    for l, r in queries:
      k = prefix_nz[r + 1] - prefix_nz[l]
      x = (prefix_x[r + 1] - prefix_x[l] * pow(10, k, MOD)) % MOD
      digit_sum = prefix_sum[r + 1] - prefix_sum[l]
      results.append(x * digit_sum % MOD)

    return results


print(Solution().sumAndMultiply("10203004", [[0, 7], [1, 3], [4, 6]]))  # [12340, 4, 9]
print(Solution().sumAndMultiply("1000", [[0, 3], [1, 1]]))              # [1, 0]
print(Solution().sumAndMultiply("9876543210", [[0, 9]]))                # [444444137]