class AutoIncrementID():
    id: int

    def __init__(self):
        self.id = -1

    def increment(self):
        self.id += 1
        return self.id
