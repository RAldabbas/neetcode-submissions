class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carStack = []
        cars = sorted(zip(position, speed), reverse=True)
        numFleets = 0
        for pos, speed in cars:
            carTime = (target - pos) / speed
            if carStack and carTime <= carStack[-1]:
                continue
            carStack.append(carTime)
        return len(carStack)
        


        