class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        myStack = []
        res = [0] * len(temperatures)
        
        for i, num in enumerate(temperatures):
            while myStack and num > temperatures[myStack[-1]]:
                temp = myStack.pop()
                res[temp] = i - temp
            myStack.append(i)
        
        return res


