class MinStack:

    def __init__(self):
        self.items = []
        self.mins = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.mins:
            self.mins.append(val)
        elif val < self.mins[-1]:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])


    def pop(self) -> None:
        self.mins.pop(-1)
        return self.items.pop(-1)


    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.mins[-1]
