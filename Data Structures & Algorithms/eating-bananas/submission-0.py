class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best = right

        while left <= right:
            rate = (left + right) // 2
            tot = sum(math.ceil(x / rate) for x in piles)
            print(rate)
            print(tot)

            if tot <= h:
                best = rate
                right = rate - 1
            else:
                left = rate + 1

            
                
        return best
        