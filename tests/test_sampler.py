class FakeProbe:
    def __init__(self, values):
        self._values = iter(values)

    def sample(self):
        return next(self._values)

def test_sampler_tick_appends_values():
    from latviz.buffer import RingBuffer
    from latviz.sampler import Sampler

    probe = FakeProbe([10, 20, 30])
    buffer = RingBuffer(5)
    sampler = Sampler(probe, buffer, interval=0)

    sampler.tick()
    sampler.tick()
    sampler.tick()

    assert buffer.values() == [10, 20, 30]
