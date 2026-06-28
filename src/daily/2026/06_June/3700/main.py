class Solution:
  def zigZagArrays(self, n: int, l: int, r: int) -> int:
    """
    3700. Number of ZigZag Arrays II

    Same zigzag DP as 3699 but n up to 10^9, m = r-l+1 up to 74.
    Exploit symmetry down[v] = up[m-1-v] to reduce the state to just up[v].
    The transition T[v][w] = 1 iff v + w >= m. Apply T^(n-2) via matrix
    exponentiation, then answer = 2 * sum(result).

    Time: O(m^3 log n) — matrix exponentiation on m×m matrix.
    Space: O(n^2).
    """
    MOD = 10 ** 9 + 7
    m = r - l + 1

    def mat_mul(A, B):
      BT = list(zip(*B))
      return [[sum(a * b for a, b in zip(row, col)) % MOD for col in BT] for row in A]

    def mat_pow(M, p):
      sz = len(M)
      res = [[int(i == j) for j in range(sz)] for i in range(sz)]
      while p:
        if p & 1:
          res = mat_mul(res, M)
        M = mat_mul(M, M)
        p >>= 1
      return res

    T = [[1 if v + w >= m else 0 for w in range(m)] for v in range(m)]
    Tn = mat_pow(T, n - 2)

    base = list(range(m))
    total = 0
    for i in range(m):
      total += sum(Tn[i][j] * base[j] for j in range(m))
    return 2 * total % MOD


print(Solution().zigZagArrays(3, 4, 5))  # 2
print(Solution().zigZagArrays(3, 1, 3))  # 10
