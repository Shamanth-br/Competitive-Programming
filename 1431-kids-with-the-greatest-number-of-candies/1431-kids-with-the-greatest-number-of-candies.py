class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candie = max(candies)
        result = []
        for c in candies:
            if c + extraCandies >= max_candie:
                result.append(1)
            else:
                result.append(0)
        return result