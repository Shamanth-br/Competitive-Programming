class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            while( ans and ans[-1] > 0 and a < 0):
                if ans[-1]+ a > 0:
                    break
                elif ans[-1]+a < 0:
                    ans.pop()
                else:
                    ans.pop()
                    break
            else:
                ans.append(a)
        return ans

            