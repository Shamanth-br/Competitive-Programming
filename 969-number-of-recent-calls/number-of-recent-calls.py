class RecentCounter:

    def __init__(self):
        self.start = 0
        self.record = []

    def ping(self, t: int) -> int:
        self.record.append(t)
        self.start = 0
        for time in self.record:
            if t - time <= 3000:
                self.start += 1

        return self.start

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)