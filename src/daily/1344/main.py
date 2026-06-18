class Solution:
  def angleClock(self, hour: int, minutes: int) -> float:
    """
    1344. Angle Between Hands of a Clock
    
    Angle between hands of a clock can be determined using formula |30*H - 5.5*M|,
    where H is hour and M is minutes.
    
    Time: O(1) — single formula evaluation.
    Space: O(1) — only one variable to store the result.
    """
    angle = abs(30 * hour - 5.5 * minutes)
    return angle if angle <= 180 else 360 - angle


print(Solution().angleClock(12, 30)) # 165
print(Solution().angleClock(3, 30)) # 75
print(Solution().angleClock(3, 15)) # 7.5
