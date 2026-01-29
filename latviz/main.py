import argparse
import threading

from latviz.buffer import RingBuffer
from latviz.sampler import Sampler
from latviz.probe import TCPProbe
from latviz.ui import run_plot


def main():
    args = parse_args()

    print(f"Probing {args.host}:{args.port} every {args.interval}s")

    buffer = RingBuffer(args.buffer)

    probe = TCPProbe(
        target=args.host,
        port=args.port,
        timeout=args.timeout,
    )

    sampler = Sampler(
        probe=probe,
        buffer=buffer,
        interval=args.interval,
    )

    thread = threading.Thread(target=sampler.run, daemon=True)
    thread.start()

    try:
        run_plot(buffer, on_close=sampler.stop)
    finally:
        sampler.stop()


def parse_args():
    parser = argparse.ArgumentParser(
        description="TCP latency visualizer"
    )

    parser.add_argument(
        "--host",
        default="8.8.8.8",
        help="Target host (default: 8.8.8.8)",
    )

    parser.add_argument(
        "--port",
        type=int,
        default=443,
        help="TCP port (default: 443)",
    )

    parser.add_argument(
        "--interval",
        type=float,
        default=1.0,
        help="Sampling interval in seconds (default: 1.0)",
    )

    parser.add_argument(
        "--buffer",
        type=int,
        default=100,
        help="Number of samples to keep (default: 100)",
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=1.0,
        help="TCP timeout in seconds (default: 1.0)",
    )

    return parser.parse_args()


if __name__ == "__main__":
    main()
