# Crowtime

`Crowtime` is an experimental Python-based network latency visualizer.  
The goal of the project is to provide a simple, extensible tool for measuring
and visualizing network latency over time, starting with TCP and expanding to
other protocols.

This repository currently represents **v1 / early groundwork** and is under
active development.

---

## Motivation

Network latency issues are often intermittent and difficult to reason about
from single measurements. Tools like `ping` are useful, but they don’t always
tell the full story—especially for application-level behavior.

`Crowtime` was created to:
- Continuously sample network latency
- Visualize trends, spikes, and packet loss over time
- Provide a foundation for experimenting with different probing methods
  (TCP, UDP, ICMP)

The long-term vision is a lightweight, developer-friendly latency visualization
tool that works well on desktops and servers alike.

---

## Quick Start

> ⚠️ **Note:** This project is currently experimental and may require some
> manual setup depending on your environment.

Clone the repository:

git clone https://github.com/Yssengrim/crowtime.git
cd crowsight

Create and activate a virtual environment, then install dependencies:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Run the visualizer:

python main.py

## Usage

Basic usage:

python main.py --host 1.1.1.1 --port 443 --interval 1.0


Available options:

--host – Target host to probe (default: 8.8.8.8)

--port – TCP port to connect to (default: 443)

--interval – Sampling interval in seconds

--buffer – Number of samples to retain

--timeout – TCP connection timeout in seconds

Current features:

TCP-based latency sampling

Background sampling thread

Fixed-size ring buffer

Live matplotlib visualization with basic statistics

Known limitations:

GUI backend support may vary by platform

Matplotlib stability is still being worked on

API and internal structure are subject to change

## Contributing

Contributions are welcome, especially while the project is still taking shape.

Good places to help:

Stabilizing the visualization backend

Improving test coverage

Adding alternative output modes (headless, CSV, logs)

Designing support for additional protocols (UDP, ICMP)

If you’d like to contribute:

Fork the repository

Create a feature branch

Keep changes small and focused

Open a pull request with a clear description

If you’re unsure where to start, feel free to open an issue to discuss ideas or
direction.

