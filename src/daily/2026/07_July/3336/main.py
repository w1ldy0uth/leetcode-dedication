from collections import Counter
from math import gcd
from typing import List

MOD = 10**9 + 7


class Solution:
  def subsequencePairCount(self, nums: List[int]) -> int:
    """
    3336. Find the Number of Subsequences With Equal GCD

    For d | gcd(A), d must divide every element of A (since gcd(A) divides
    each element, and any divisor of gcd(A) transitively divides them too).
    So instead of grouping by a common gcd value g directly, fix g and look
    only at elements divisible by g, reduced to v // g. We need disjoint
    nonempty (A, B) with gcd(A) == gcd(B) == 1 among these reduced values.

    Use the Mobius identity [gcd(S) == 1] = sum_{d | gcd(S)} mu(d) to turn
    this into a sum over divisor pairs (d1, d2): for fixed d1, d2, count
    disjoint nonempty (A, B) where every element of A is divisible by d1
    and every element of B is divisible by d2. Splitting the eligible
    elements into "divisible by both" (b), "only d1" (o1), "only d2" (o2)
    gives, by inclusion-exclusion on emptiness:
      ways = 3^b * 2^o1 * 2^o2 - 2^b*2^o2 - 2^b*2^o1 + 1
    Summing mu(d1)*mu(d2)*ways over all d1, d2 (skipping mu == 0) yields the
    exact-gcd-1 pair count for this g; summing over all g gives the answer.

    Time: ~ O(m^3 log maxVal)
    Space: O(m)
    """
    max_val = max(nums)

    mu = [1] * (max_val + 1)
    mu[0] = 0
    is_composite = [False] * (max_val + 1)
    primes = []
    for i in range(2, max_val + 1):
      if not is_composite[i]:
        primes.append(i)
        mu[i] = -1
      for p in primes:
        if i * p > max_val:
          break
        is_composite[i * p] = True
        if i % p == 0:
          mu[i * p] = 0
          break
        mu[i * p] = -mu[i]

    val_count = Counter(nums)
    answer = 0

    for g in range(1, max_val + 1):
      max_reduced = max_val // g
      if max_reduced == 0:
        continue

      freq = [0] * (max_reduced + 1)
      total = 0
      for v, c in val_count.items():
        if v % g == 0:
          rv = v // g
          freq[rv] += c
          total += c

      if total < 2:
        continue

      cnt_div = [0] * (max_reduced + 1)
      for d in range(1, max_reduced + 1):
        cnt_div[d] = sum(freq[d::d])

      pow2 = [1] * (total + 1)
      pow3 = [1] * (total + 1)
      for i in range(1, total + 1):
        pow2[i] = pow2[i - 1] * 2 % MOD
        pow3[i] = pow3[i - 1] * 3 % MOD

      g_answer = 0
      for d1 in range(1, max_reduced + 1):
        if mu[d1] == 0 or cnt_div[d1] == 0:
          continue
        c1 = cnt_div[d1]
        for d2 in range(1, max_reduced + 1):
          if mu[d2] == 0 or cnt_div[d2] == 0:
            continue
          c2 = cnt_div[d2]
          lc = d1 * d2 // gcd(d1, d2)
          both = cnt_div[lc] if lc <= max_reduced else 0
          only1 = c1 - both
          only2 = c2 - both
          ways = (
              pow3[both] * pow2[only1] % MOD * pow2[only2]
              - pow2[both] * pow2[only2]
              - pow2[both] * pow2[only1]
              + 1
          ) % MOD
          g_answer = (g_answer + mu[d1] * mu[d2] * ways) % MOD

      answer = (answer + g_answer) % MOD

    return answer % MOD


print(Solution().subsequencePairCount([1, 2, 3, 4]))  # 10
print(Solution().subsequencePairCount([10, 20, 30]))  # 2
print(Solution().subsequencePairCount([1, 1, 1, 1]))  # 50
