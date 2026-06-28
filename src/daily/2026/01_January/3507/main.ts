/**
 * 3507. Minimum Pair Removal to Sort Array I
 *
 * We check in a loop if an array is sorted and if not we try to brute-force an array to find the minimal sum pair and replace its values by its sum.
 * Loop runs until an array becomes sorted. Also paying attention to edges to not end up with NaN.
 * @param nums an initial array of numbers to make non-decreasing.
 * @returns a minimal amount of operations to make nums a non-decreasing array.
 */
const minimumPairRemoval = (nums: number[]): number => {
  let ops = 0;

  const isNonDecreasing = (arr: number[]): boolean =>
    arr.every((val, idx, arr) => idx === 0 || val >= arr[idx - 1]);

  const replaceMinimumPair = (arr: number[]): void => {
    let minPairSum =
        Math.min(...arr) + arr[arr.indexOf(Math.min(...arr)) + 1] <
          Math.min(...arr) + arr[arr.indexOf(Math.min(...arr)) - 1] &&
        !isNaN(Math.min(...arr) + arr[arr.indexOf(Math.min(...arr)) - 1])
          ? Math.min(...arr) + arr[arr.indexOf(Math.min(...arr)) + 1]
          : !isNaN(Math.min(...arr) + arr[arr.indexOf(Math.min(...arr)) - 1])
            ? Math.min(...arr) + arr[arr.indexOf(Math.min(...arr)) - 1]
            : Math.min(...arr) + arr[arr.indexOf(Math.min(...arr)) + 1],
      minIdx =
        Math.min(...arr) + arr[arr.indexOf(Math.min(...arr)) + 1] <
          Math.min(...arr) + arr[arr.indexOf(Math.min(...arr)) - 1] &&
        !isNaN(Math.min(...arr) + arr[arr.indexOf(Math.min(...arr)) - 1])
          ? arr.indexOf(Math.min(...arr)) + 1
          : arr.indexOf(Math.min(...arr)) > 0
            ? arr.indexOf(Math.min(...arr))
            : arr.indexOf(Math.min(...arr)) + 1;

    arr.forEach((_, idx) => {
      if (
        idx !== 0 &&
        (arr[idx] + arr[idx - 1] < minPairSum ||
          (arr[idx] + arr[idx - 1] === minPairSum && idx < minIdx))
      )
        ((minIdx = idx), (minPairSum = arr[idx] + arr[idx - 1]));
    });

    arr[minIdx - 1] = minPairSum;
    arr.splice(minIdx, 1);
  };

  while (!isNonDecreasing(nums)) {
    replaceMinimumPair(nums);
    ++ops;
  }
  return ops;
};

console.log(minimumPairRemoval([1, 2, 2]));
console.log(minimumPairRemoval([5, 2, 3, 1])); // ans -> 2
console.log(minimumPairRemoval([2, 2, -1, 3, -2, 2, 1, 1, 1, 0, -1])); // ans -> 9
console.log(minimumPairRemoval([1, 1, 4, 4, 2, -4, -1])); // ans -> 5
console.log(minimumPairRemoval([2, 1])); // ans -> 1
console.log(minimumPairRemoval([0, 1, 1, 2, -1, 1])); // ans -> 4
