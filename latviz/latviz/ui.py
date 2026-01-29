import matplotlib
matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def compute_stats(values):
    valid = [v for v in values if v is not None]
    total = len(values)

    if total == 0:
        return None, None, 0.0

    last = valid[-1] if valid else None
    avg = sum(valid) / len(valid) if valid else None
    loss = 1.0 - (len(valid) / total)

    return last, avg, loss * 100


def run_plot(buffer, interval_ms=1000, on_close=None):
    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)

    ax.set_title("TCP Latency (ms)")
    ax.set_xlabel("Samples")
    ax.set_ylabel("Latency")

    stats_text = ax.text(
        0.02,
        0.95,
        "",
        transform=ax.transAxes,
        va="top",
        fontsize=10,
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
    )

    def update(_):
        data = buffer.values()
        if not data:
            return line, stats_text

        x = list(range(len(data)))
        y = data

        line.set_data(x, y)

        # --- clamp axes ---
        ax.set_xlim(0, buffer.size)

        valid = [v for v in y if v is not None]
        if valid:
            ymax = max(10, max(valid) * 1.2)
            ax.set_ylim(0, ymax)

        last, avg, loss = compute_stats(y)

        lines = []
        if last is not None:
            lines.append(f"Last: {last:.1f} ms")
        if avg is not None:
            lines.append(f"Avg: {avg:.1f} ms")
        lines.append(f"Loss: {loss:.1f}%")

        stats_text.set_text("\n".join(lines))

        return line, stats_text

    anim = animation.FuncAnimation(
        fig,
        update,
        interval=interval_ms,
        cache_frame_data=False,
    )

    def _on_close(event):
        if on_close:
            on_close()

    fig.canvas.mpl_connect("close_event", _on_close)

    plt.show()
