/**
 * 3379. Transformed Array
 *
 * We traverse an array as usual and apply modulo logic to find the resulting index.
 * @param nums - The input array
 * @returns - The transformed array
 */
function constructTransformedArray(nums: number[]): number[] {
  const n = nums.length;
  const result: number[] = new Array(n);

  for (let i = 0; i < n; i++) {
    if (nums[i] === 0) {
      result[i] = 0;
    } else {
      let steps = nums[i];
      let index = i;

      if (steps > 0) {
        index = (index + steps) % n;
      } else {
        index = (index + steps) % n;
        if (index < 0) {
          index += n;
        }
      }

      result[i] = nums[index];
    }
  }

  return result;
}

console.log(constructTransformedArray([3, -2, 1, 1])); // [1,1,1,3]
