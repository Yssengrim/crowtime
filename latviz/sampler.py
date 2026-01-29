import time
import threading

class Sampler:
    def __init__(self, probe, buffer, interval):
        self.probe = probe
        self.buffer = buffer
        self.interval = interval
        self._stop_event = threading.Event()

    def tick(self):
        latency = self.probe.sample()
        self.buffer.push(latency)

    def run(self):
        while not self._stop_event.is_set():
            try:
                self.tick()
            except Exception as e:
                # don't kill the thread on probe errors
                self.buffer.push(None)
            time.sleep(self.interval)

    def stop(self):
        self._stop_event.set()
