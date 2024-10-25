class RecentCounter:
    def __init__(self):
        self.times = []

    def ping(self, t: int) -> int:
        self.times.append(t)
        
        counter = 0
        base = t-3000

        while (self.times[counter] < base):
            counter += 1
        
        self.times = self.times[counter:]
        
        return len(self.times)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)