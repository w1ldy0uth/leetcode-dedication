/**
 * 1732. Find the Highest Altitude
 *
 * Compute a running prefix sum of gains, tracking the maximum altitude seen.
 * The starting altitude is 0, which may itself be the highest point.
 *
 * Time: O(n) — single pass through the gain array.
 * Space: O(1) — only two variables for current altitude and max.
 */
const largestAltitude = (gain: number[]): number => {
  let max = 0;
  let alt = 0;

  for (const g of gain) {
    alt += g;
    if (alt > max) max = alt;
  }

  return max;
}

console.log(largestAltitude([-5, 1, 5, 0, -7])); // 1
console.log(largestAltitude([-4, -3, -2, -1, 4, 3, 2])); // 0
