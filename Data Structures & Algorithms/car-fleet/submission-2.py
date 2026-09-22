class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        numFleets = 0
        maxTime = 0.0
        for pos, speed in cars:
            carTime = (target - pos) / speed
            if carTime > maxTime:
                numFleets += 1
                maxTime = carTime
        return numFleets
        
