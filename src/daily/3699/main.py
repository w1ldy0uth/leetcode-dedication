class Solution:
  def zigZagArrays(self, n: int, l: int, r: int) -> int:
    """
    3699. Number of ZigZag Arrays I

    Every interior element must be a local min or max (zigzag pattern).
    Track dp_up[v] / dp_down[v] = arrays ending at value v with last step
    going up / down. Transition via prefix/suffix sums of the opposite array:
    new_up[v] = prefix_down[v-1], new_down[v] = suffix_up[v+1].

    Time: O(n * m) where m = r - l + 1.
    Space: O(n).
    """
    MOD = 10 ** 9 + 7
    m = r - l + 1

    up = list(range(m))
    down = list(range(m - 1, -1, -1))

    for _ in range(3, n + 1):
      pre = [0] * (m + 1)
      for v in range(m):
        pre[v + 1] = (pre[v] + down[v]) % MOD

      suf = [0] * (m + 1)
      for v in range(m - 1, -1, -1):
        suf[v] = (suf[v + 1] + up[v]) % MOD

      up = [pre[v] for v in range(m)]
      down = [suf[v + 1] for v in range(m)]

    return (sum(up) + sum(down)) % MOD


print(Solution().zigZagArrays(3, 4, 5))  # 2
print(Solution().zigZagArrays(3, 1, 3))  # 10
