from latviz.buffer import RingBuffer


def test_ring_buffer_rollover():
    buf = RingBuffer(3)
    buf.push(1)
    buf.push(2)
    buf.push(3)
    buf.push(4)

    assert buf.values() == [2, 3, 4]
