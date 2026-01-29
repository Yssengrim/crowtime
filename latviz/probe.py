# latviz/probe.py
from abc import ABC, abstractmethod
import socket
import time

class Probe(ABC):
    def __init__(self, target: str):
        self.target = target

    @abstractmethod
    def sample(self) -> float | None:
        """
        Return latency in milliseconds.
        Return None on timeout or failure.
        """
        raise NotImplementedError


class TCPProbe(Probe):
    def __init__(self, target: str, port: int = 443, timeout: float = 1.0):
        super().__init__(target)
        self.port = port
        self.timeout = timeout

    def sample(self) -> float | None:
        start = time.perf_counter()
        try:
            with socket.create_connection(
                (self.target, self.port),
                timeout=self.timeout
            ):
                end = time.perf_counter()
                return (end - start) * 1000
        except OSError:
            return None
