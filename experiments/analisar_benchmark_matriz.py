from __future__ import annotations

import csv
import os
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "work" / "matplotlib-cache"))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


INPUT = ROOT / "data" / "benchmark_matriz_numpy.csv"
SUMMARY = ROOT / "data" / "benchmark_matriz_resumo.csv"
FIGURE = ROOT / "paper" / "figures" / "benchmark-gflops.png"


def load_rows() -> list[dict[str, str]]:
    with INPUT.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def summarize(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    summary: list[dict[str, str]] = []
    sizes = sorted({int(row["size"]) for row in rows})
    for size in sizes:
        group = [row for row in rows if int(row["size"]) == size]
        elapsed = [float(row["elapsed_seconds"]) for row in group]
        gflops = [float(row["estimated_gflops"]) for row in group]
        summary.append(
            {
                "size": str(size),
                "repetitions": str(len(group)),
                "elapsed_mean_seconds": f"{statistics.mean(elapsed):.6f}",
                "elapsed_stdev_seconds": f"{statistics.stdev(elapsed):.6f}",
                "gflops_mean": f"{statistics.mean(gflops):.3f}",
                "gflops_stdev": f"{statistics.stdev(gflops):.3f}",
            }
        )
    return summary


def write_summary(rows: list[dict[str, str]]) -> None:
    SUMMARY.parent.mkdir(parents=True, exist_ok=True)
    with SUMMARY.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "size",
                "repetitions",
                "elapsed_mean_seconds",
                "elapsed_stdev_seconds",
                "gflops_mean",
                "gflops_stdev",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def draw_chart(rows: list[dict[str, str]]) -> None:
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    labels = [f"{row['size']}x{row['size']}" for row in rows]
    means = [float(row["gflops_mean"]) for row in rows]
    stdevs = [float(row["gflops_stdev"]) for row in rows]

    fig, ax = plt.subplots(figsize=(8, 4.8), dpi=180)
    bars = ax.bar(labels, means, yerr=stdevs, capsize=6, color="#2f66a3", edgecolor="#1d3557")

    ax.set_title("Desempenho médio por ordem da matriz")
    ax.set_xlabel("Ordem da matriz")
    ax.set_ylabel("GFLOPS")
    ax.grid(axis="y", alpha=0.25)
    ax.set_axisbelow(True)

    for bar, value in zip(bars, means):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 8,
            f"{value:.1f}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    fig.tight_layout()
    fig.savefig(FIGURE)
    plt.close(fig)


def main() -> None:
    rows = summarize(load_rows())
    write_summary(rows)
    draw_chart(rows)
    print(f"Resumo gerado: {SUMMARY}")
    print(f"Figura gerada: {FIGURE}")


if __name__ == "__main__":
    main()
