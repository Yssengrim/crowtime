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

```bash
git clone 
cd crowsight
