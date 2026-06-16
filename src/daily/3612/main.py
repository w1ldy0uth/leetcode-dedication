class Solution:
  def processStr(self, s: str) -> str:
    """
    3612. Process String with Special Operations I

    Simulate left-to-right: maintain a list buffer and apply each operation
    directly — pop for '*', extend with a copy for '#', reverse in-place for '%'.

    Time: O(n * 2^n) — each '#' doubles the buffer, so n '#' ops cost 1+2+4+...+2^n.
    Space: O(2^n) — buffer size after n '#' operations.
    """
    res = []
    for c in s:
      if c == '*':
        if res:
          res.pop()
      elif c == '#':
        res += res[:]
      elif c == '%':
        res.reverse()
      else:
        res.append(c)
    return ''.join(res)


print(Solution().processStr("a#b%*"))  # "ba"
print(Solution().processStr("z*#"))   # ""
