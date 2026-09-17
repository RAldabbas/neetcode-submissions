class MinStack:

    def __init__(self):
        self.items = []
        self.mins = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.mins:
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.mins[-1]))


    def pop(self) -> None:
        self.mins.pop()
        return self.items.pop()


    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.mins[-1]
