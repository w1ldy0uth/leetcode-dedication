/**
 * 3637. Trionic Array I.
 *
 * We should treat an array as a function with two local extrema: one local maximum
 * and one local minimum. An array is called trionic if it has exactly one local maximum
 * followed by exactly one local minimum. Thus, we need to find those extrema and ensure
 * that the rest of the array is strictly increasing.
 * @param nums - the input array of numbers.
 * @returns true if the array is trionic, false otherwise.
 */
function isTrionic(nums: number[]): boolean {
  if (nums.length < 3) return false;

  let peak = 0;
  while (peak < nums.length - 1 && nums[peak] < nums[peak + 1]) {
    peak++;
  }
  if (peak === 0 || peak === nums.length - 1) return false;

  let valley = peak;
  while (valley < nums.length - 1 && nums[valley] > nums[valley + 1]) {
    valley++;
  }
  if (valley === peak || valley === nums.length - 1) return false;

  for (let i = valley; i < nums.length - 1; i++) {
    if (nums[i] >= nums[i + 1]) {
      return false;
    }
  }

  return true;
}

console.log(isTrionic([1, 3, 5, 4, 2, 6])); // true
console.log(isTrionic([2, 1, 3])); // false
console.log(isTrionic([4, 4, 7])); // false
