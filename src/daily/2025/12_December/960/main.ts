/**
 * 960. Delete Columns to Make Sorted III
 *
 * We must delete the same set of column indices from every string.
 * After deletions, each remaining row must be nondecreasing left-to-right.
 */
const minDeletionSize = (strs: string[]): number => {
  const n = strs.length;
  const m = strs[0]?.length ?? 0;
  if (m <= 1) return 0;

  const dp = new Array<number>(m).fill(1);
  let best = 1;

  for (let j = 0; j < m; ++j) {
    for (let i = 0; i < j; ++i) {
      let ok = true;
      for (let r = 0; r < n; r++) {
        if (strs[r][i] > strs[r][j]) {
          ok = false;
          break;
        }
      }
      if (ok) dp[j] = Math.max(dp[j], dp[i] + 1);
    }
    best = Math.max(best, dp[j]);
  }

  return m - best;
}

// Test cases
console.log(minDeletionSize(["babca", "bbazb"])); // 3
console.log(minDeletionSize(["edcba"])); // 4
console.log(minDeletionSize(["ghi", "def", "abc"])); // 0

