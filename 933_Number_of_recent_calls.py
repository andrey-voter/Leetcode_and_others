from collections import deque


class RecentCounter:

    def __init__(self):
        self.calls = deque()
        self.n = 3000

    def ping(self, t: int) -> int:
        self.calls.append(t)
        while self.calls[0] < t - self.n:
            self.calls.popleft()
        return len(self.calls)


class RecentCounter2:

    def __init__(self):
        self.calls = []
        self.n = 3000

    def ping(self, t: int) -> int:
        self.calls.append(t)
        non_relevant = 0
        for call in self.calls:
            if call < t - self.n:
                non_relevant += 1
            else:
                break
        self.calls = self.calls[non_relevant:]
        return len(self.calls)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)