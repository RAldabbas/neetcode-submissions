class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        myStack = []
        res = [0] * len(temperatures)
        
        for i, num in enumerate(temperatures):
            while myStack and num > myStack[-1][1]:
                temp = myStack.pop()
                res[temp[0]] = i - temp[0]
            myStack.append((i, num))
        
        return res


