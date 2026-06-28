/**
 * 3315. Construct the Minimum Bitwise Array II
 *
 * We must iterate through each member of nums and try applying smallest possible bitwise suffixes to it.
 * At each step of a while loop we shift suffix at one bit to the left (bitwise 1, 10, 100) until the suffix don't overcome the original number.
 * @param nums an array of given prime numbers
 * @returns an answer array where each ans[i] is determined as (ans[i] OR (ans[i] + 1) === nums[i])
 */
const minBitwiseArray = (nums: number[]): number[] => {
  nums.forEach((num, idx) => {
    let res = -1;
    let suffix = 1;
    while ((num & suffix) !== 0) {
      res = num - suffix;
      suffix = suffix << 1;
    }
    nums[idx] = res;
  });
  return nums;
};

console.log(minBitwiseArray([2, 3, 5, 7]));
console.log(minBitwiseArray([11, 13, 31]));
