from collections import deque
from typing import List


class Solution:
  def remainingMethods(
      self,
      n: int,
      k: int,
      invocations: List[List[int]]
  ) -> List[int]:
    """
    3310. Remove Methods From Project

    Identify suspicious nodes via BFS and check for external incoming edges.

    Time: O(n + m)
    Space: O(n + m)
    """
    graph = [[] for _ in range(n)]

    for caller, callee in invocations:
      graph[caller].append(callee)

    suspicious = [False] * n
    suspicious[k] = True

    queue = deque([k])

    while queue:
      method = queue.popleft()

      for invoked_method in graph[method]:
        if not suspicious[invoked_method]:
          suspicious[invoked_method] = True
          queue.append(invoked_method)

    for caller, callee in invocations:
      if not suspicious[caller] and suspicious[callee]:
        return list(range(n))

    return [
        method
        for method in range(n)
        if not suspicious[method]
    ]


print(Solution().remainingMethods(
    4, 1, [[1, 2], [0, 1], [3, 2]]))  # Output: [0,1,2,3]
print(Solution().remainingMethods(
    5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]]))  # Output: [3,4]
print(Solution().remainingMethods(
    3, 2, [[1, 2], [0, 1], [2, 0]]))  # Output: []
