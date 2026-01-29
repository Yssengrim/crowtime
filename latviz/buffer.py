class RingBuffer:
    def __init__(self, size):
        self.size = size
        self._data = []

    def push(self, value):
        self._data.append(value)
        if len(self._data) > self.size:
            self._data.pop(0)

    def values(self):
        return list(self._data)
