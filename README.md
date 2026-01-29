# CrowTime

`CrowTime` is a lightweight TCP latency visualizer written in Python.  
It measures connection latency to a target host and displays the results in a live, updating graph.

This project is currently in **early development (v1)** and focuses on establishing a clean, extensible foundation.

---

## What It Does

- Measures TCP connection latency to a target host
- Samples latency at a configurable interval
- Stores recent samples in a fixed-size ring buffer
- Displays latency in real time using `matplotlib`
- Tracks packet loss when probes fail

---

## Getting Started

### Requirements

- Python 3.10 or newer
- `matplotlib`

> **Note**  
> Graph rendering depends on your system’s GUI backend (Tk / Qt).
> If the window does not open, the issue is usually related to the Python distribution or GUI backend rather than `CrowTime itself.

---

### Running CrowTime

Run with default settings:

```bash
python main.py
