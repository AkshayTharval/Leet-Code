class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import deque
        from collections import Counter

        self.capacity   = capacity
        self.cache      = dict()
        self.keyQueue   = deque()
        self.keyCounter = Counter()

    def _shrinkKeyQueue(self):

        if len(self.keyQueue) > 2 * self.capacity:
            self.keyCounter.clear()

            from collections import deque

            newKeyQueue = deque()
            while len(self.keyCounter) < len(self.cache):
                key = self.keyQueue.pop()
                if key not in self.keyCounter:
                    self.keyCounter[key] += 1
                    newKeyQueue.appendleft(key)

            self.keyQueue.clear()
            self.keyQueue = newKeyQueue

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            self.keyQueue.append(key)
            self.keyCounter[key] += 1

            self._shrinkKeyQueue()

            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        self.cache[key] = value
        self.keyQueue.append(key)
        self.keyCounter[key] += 1

        while len(self.cache) > self.capacity:
            oldestKey = self.keyQueue.popleft()
            self.keyCounter[oldestKey] -= 1
            if self.keyCounter[oldestKey]==0:
                del self.keyCounter[oldestKey]
                del self.cache[oldestKey]

        self._shrinkKeyQueue()