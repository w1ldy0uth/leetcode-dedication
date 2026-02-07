/**
 * 1653. Minimum Deletions to Make String Balanced
 *
 * We simply removing every b char from the beginning of the string.
 * @param s - an input string
 * @returns - an amount of minimum deletions to make string balanced
 */
function minimumDeletions(s: string): number {
  let aCount = 0;
  let bCount = 0;
  let deletions = 0;

  for (const char of s) {
    if (char === "a") {
      if (bCount > 0) {
        bCount--;
        deletions++;
      } else {
        aCount++;
      }
    } else {
      bCount++;
    }
  }

  return deletions;
}

console.log(minimumDeletions("aababbab")); // 2
