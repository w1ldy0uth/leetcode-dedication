from collections import Counter
from typing import List


class Solution:
  def findSubstring(self, s: str, words: List[str]) -> List[int]:
    """
    30. Substring with Concatenation of All Words

    since every word has the same length m, any valid substring is aligned to word boundaries starting at some offset r = start % m.
    So run a sliding window separately for each of the m possible remainders.

    Time: O(n * m) where n is the length of s and m is the number of words
    Space: O(m) where m is the number of words
    """
    if not s or not words:
      return []

    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    n = len(s)

    if n < total_len:
      return []

    word_count = Counter(words)
    result = []

    for r in range(word_len):
      left = r
      count = 0
      window = Counter()

      for right in range(r, n - word_len + 1, word_len):
        w = s[right:right + word_len]
        if w not in word_count:
          window.clear()
          count = 0
          left = right + word_len
          continue
        window[w] += 1
        count += 1
        while window[w] > word_count[w]:
          left_w = s[left:left + word_len]
          window[left_w] -= 1
          count -= 1
          left += word_len
        if count == num_words:
          result.append(left)
          left_w = s[left:left + word_len]
          window[left_w] -= 1
          count -= 1
          left += word_len

    return result


print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))  # [0, 9]
print(Solution().findSubstring("wordgoodgoodgoodbestword",
      ["word", "good", "best", "word"]))  # []
print(Solution().findSubstring("barfoofoobarthefoobarman",
      ["bar", "foo", "the"]))  # [6, 9, 12]
