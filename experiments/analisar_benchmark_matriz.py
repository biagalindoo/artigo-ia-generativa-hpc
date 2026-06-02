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
from scipy import stats


INPUT = ROOT / "data" / "benchmark_matriz_numpy.csv"
SUMMARY = ROOT / "data" / "benchmark_matriz_resumo.csv"
TESTS = ROOT / "data" / "benchmark_matriz_testes.csv"
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
        n = len(group)
        t_critical = stats.t.ppf(0.975, df=n - 1)
        gflops_ci95 = t_critical * statistics.stdev(gflops) / (n**0.5)
        elapsed_ci95 = t_critical * statistics.stdev(elapsed) / (n**0.5)
        summary.append(
            {
                "size": str(size),
                "repetitions": str(n),
                "warmups_discarded": group[0].get("warmups_discarded", "0"),
                "elapsed_mean_seconds": f"{statistics.mean(elapsed):.6f}",
                "elapsed_stdev_seconds": f"{statistics.stdev(elapsed):.6f}",
                "elapsed_ci95_seconds": f"{elapsed_ci95:.6f}",
                "gflops_mean": f"{statistics.mean(gflops):.3f}",
                "gflops_stdev": f"{statistics.stdev(gflops):.3f}",
                "gflops_ci95": f"{gflops_ci95:.3f}",
            }
        )
    return summary


def hypothesis_tests(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    tests: list[dict[str, str]] = []
    sizes = sorted({int(row["size"]) for row in rows})
    for left, right in zip(sizes, sizes[1:]):
        left_values = [float(row["estimated_gflops"]) for row in rows if int(row["size"]) == left]
        right_values = [float(row["estimated_gflops"]) for row in rows if int(row["size"]) == right]
        result = stats.ttest_ind(left_values, right_values, equal_var=False)
        tests.append(
            {
                "comparison": f"{left}_vs_{right}",
                "test": "Welch t-test",
                "statistic": f"{result.statistic:.6f}",
                "p_value": f"{result.pvalue:.6e}",
                "alpha": "0.05",
                "reject_h0": str(result.pvalue < 0.05),
            }
        )
    return tests


def write_summary(rows: list[dict[str, str]]) -> None:
    SUMMARY.parent.mkdir(parents=True, exist_ok=True)
    with SUMMARY.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "size",
                "repetitions",
                "warmups_discarded",
                "elapsed_mean_seconds",
                "elapsed_stdev_seconds",
                "elapsed_ci95_seconds",
                "gflops_mean",
                "gflops_stdev",
                "gflops_ci95",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


def write_tests(rows: list[dict[str, str]]) -> None:
    TESTS.parent.mkdir(parents=True, exist_ok=True)
    with TESTS.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["comparison", "test", "statistic", "p_value", "alpha", "reject_h0"],
        )
        writer.writeheader()
        writer.writerows(rows)


def draw_chart(rows: list[dict[str, str]]) -> None:
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    labels = [f"{row['size']}x{row['size']}" for row in rows]
    means = [float(row["gflops_mean"]) for row in rows]
    errors = [float(row["gflops_ci95"]) for row in rows]

    fig, ax = plt.subplots(figsize=(8, 4.8), dpi=180)
    bars = ax.bar(labels, means, yerr=errors, capsize=6, color="#2f66a3", edgecolor="#1d3557")

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
    raw_rows = load_rows()
    rows = summarize(raw_rows)
    tests = hypothesis_tests(raw_rows)
    write_summary(rows)
    write_tests(tests)
    draw_chart(rows)
    print(f"Resumo gerado: {SUMMARY}")
    print(f"Testes gerados: {TESTS}")
    print(f"Figura gerada: {FIGURE}")


if __name__ == "__main__":
    main()
