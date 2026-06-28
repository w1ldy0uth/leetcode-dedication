class Solution:
  def processStr(self, s: str, k: int) -> str:
    """
    3612. Process String with Special Operations II
    
    Simulate left-to-right to find the final length of the processed string, then
    simulate right-to-left to remap k to the initial position in the original string.
    
    Time: O(n) — two passes through the string.
    Space: O(1) — only a few variables to track the length and pointer.
    """
    length = len(s)
    ptr = 0
    for i in s:
      if i == '*':
        if ptr > 0:
          ptr -= 1
      elif i == '#':
        ptr *= 2
      elif i == '%':
        pass
      else:
        ptr += 1
    
    if (k >= ptr):
      return "."
    
    for i in range(length - 1, -1, -1):
      if s[i] == '*':
        ptr += 1
      elif s[i] == '%':
        k = ptr - 1 - k
      elif s[i] == '#':
        ptr //= 2
        k = k - ptr if k >= ptr else k
      else:
        ptr -= 1
      
      if k == ptr:
        return s[i]
    
    return "."


print(Solution().processStr("a#b%*", 1))  # "a"
print(Solution().processStr("cd%#*#", 3))  # "b"
print(Solution().processStr("z*#", 0))   # "."