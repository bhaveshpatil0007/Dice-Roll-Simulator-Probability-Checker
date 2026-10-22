"""Simulate a fair die and visualize the law of large numbers."""
from pathlib import Path
import argparse
import csv
import numpy as np
import matplotlib.pyplot as plt

DEFAULT_SIZES = (10, 1_000, 100_000)
THEORETICAL = 1 / 6

def simulate(sample_sizes=DEFAULT_SIZES, seed=42):
    """Use nested prefixes of one seeded sequence of independent fair rolls."""
    sizes = tuple(sample_sizes)
    if not sizes or any(not isinstance(n, (int, np.integer)) or n <= 0 for n in sizes):
        raise ValueError("Sample sizes must be positive integers.")
    rng = np.random.default_rng(seed)
    rolls = rng.integers(1, 7, size=max(sizes))
    results = []
    for n in sizes:
        counts = np.bincount(rolls[:n], minlength=7)[1:7]
        results.append({"n": int(n), "counts": counts, "probabilities": counts / n})
    return rolls, results

def save_results(rolls, results, output_dir, show=False):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "frequencies.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["rolls", "face", "count", "observed_probability", "theoretical_probability", "absolute_error"])
        for result in results:
            for face, (count, probability) in enumerate(zip(result["counts"], result["probabilities"]), 1):
                writer.writerow([result["n"], face, int(count), float(probability), THEORETICAL, abs(probability-THEORETICAL)])
    plt.style.use("seaborn-v0_8-whitegrid")
    fig, axes = plt.subplots(1, len(results), figsize=(5 * len(results), 4.8), squeeze=False, sharey=True)
    colors = ["#2563eb", "#0891b2", "#059669"]
    upper = max(0.23, max(float(r["probabilities"].max()) for r in results) * 1.22)
    for i, result in enumerate(results):
        ax = axes[0, i]
        bars = ax.bar(range(1, 7), result["probabilities"] * 100, color=colors[i % len(colors)], width=0.7)
        ax.axhline(THEORETICAL * 100, color="#dc2626", linestyle="--", label="Theoretical: 16.67%")
        ax.bar_label(bars, fmt="%.2f%%", fontsize=9, padding=3)
        ax.set(title=f'{result["n"]:,} rolls', xlabel="Die face", xticks=range(1, 7), ylim=(0, upper * 100))
        ax.legend(loc="upper right", fontsize=8)
    axes[0, 0].set_ylabel("Observed frequency (%)")
    fig.suptitle("A fair die: observed frequencies approach 1/6", fontsize=16)
    fig.tight_layout()
    fig.savefig(output_dir / "probability_comparison.png", dpi=180)
    if not show:
        plt.close(fig)
    # Downsample only the plotted checkpoints; all rolls contribute to each frequency.
    checkpoints = np.unique(np.geomspace(1, len(rolls), min(1000, len(rolls))).astype(int))
    fig, ax = plt.subplots(figsize=(10, 5.5))
    for face in range(1, 7):
        cumulative = np.cumsum(rolls == face)
        ax.plot(checkpoints, cumulative[checkpoints - 1] / checkpoints * 100, label=f"Face {face}", alpha=0.85)
    ax.axhline(THEORETICAL * 100, color="black", linestyle="--", label="Theoretical: 16.67%")
    ax.set(xscale="log", xlabel="Number of rolls (log scale)", ylabel="Cumulative frequency (%)", title="Law of large numbers: convergence is not necessarily monotonic")
    ax.legend(ncol=4, fontsize=9)
    fig.tight_layout()
    fig.savefig(output_dir / "convergence.png", dpi=180)
    if not show:
        plt.close(fig)

    if show:
        plt.show()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=42, help="Random seed (default: 42)")
    parser.add_argument("--rolls", type=int, nargs="+", default=list(DEFAULT_SIZES), help="Positive sample sizes")
    parser.add_argument("--output", default=str(Path(__file__).resolve().parent), help="Directory for charts and CSV (default: script folder)")
    parser.add_argument("--no-show", action="store_true", help="Save charts without opening graph windows")
    args = parser.parse_args()
    try:
        rolls, results = simulate(args.rolls, args.seed)
    except ValueError as exc:
        parser.error(str(exc))
    save_results(rolls, results, args.output, show=not args.no_show)
    print("Theoretical probability per face: 1/6 = 16.6667%")
    for result in results:
        error = np.max(np.abs(result["probabilities"] - THEORETICAL)) * 100
        print(f'\n{result["n"]:,} rolls | maximum absolute error: {error:.4f} percentage points')
        for face, (count, probability) in enumerate(zip(result["counts"], result["probabilities"]), 1):
            print(f"  Face {face}: {int(count):>7,}  ({probability:7.2%})")
    print(f"\nCharts and CSV saved to {Path(args.output).resolve()}")

if __name__ == "__main__":
    main()
