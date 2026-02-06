/**
 * 3634. Minimum Removals to Balance Array
 * 
 * We use a sliding window to find the longest subarray which meets condition max(nums) <= min(nums) * k, 
 * and the answer is total length of nums minus length of the subarray.
 * @param nums 
 * @param k 
 * @returns 
 */
function minRemoval(nums: number[], k: number): number {
  nums.sort((a, b) => a - b);
  let maxLen = 0;
  let left = 0;

  for (let right = 0; right < nums.length; right++) {
    while (nums[right] > nums[left] * k) {
      left++;
    }
    maxLen = Math.max(maxLen, right - left + 1);
  }

  return nums.length - maxLen;
}

console.log(minRemoval([2, 1, 5], 2)); // 1
