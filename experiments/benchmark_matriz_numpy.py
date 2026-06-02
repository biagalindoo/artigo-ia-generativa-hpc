from __future__ import annotations

import csv
import platform
import time
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "benchmark_matriz_numpy.csv"


def benchmark(size: int, repetitions: int = 30, warmups: int = 5) -> list[dict[str, str]]:
    rng = np.random.default_rng(42)
    a = rng.random((size, size), dtype=np.float32)
    b = rng.random((size, size), dtype=np.float32)

    for _ in range(warmups):
        _ = a @ b

    rows: list[dict[str, str]] = []
    for rep in range(1, repetitions + 1):
        start = time.perf_counter()
        c = a @ b
        elapsed = time.perf_counter() - start

        # Matrix multiplication performs approximately 2*n^3 floating-point ops.
        gflops = (2 * size**3) / elapsed / 1e9
        rows.append(
            {
                "size": str(size),
                "repetition": str(rep),
                "warmups_discarded": str(warmups),
                "elapsed_seconds": f"{elapsed:.6f}",
                "estimated_gflops": f"{gflops:.3f}",
                "checksum": f"{float(c[0, 0]):.6f}",
            }
        )
    return rows


def main() -> None:
    rows: list[dict[str, str]] = []
    for size in (512, 1024, 2048):
        rows.extend(benchmark(size))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "size",
                "repetition",
                "warmups_discarded",
                "elapsed_seconds",
                "estimated_gflops",
                "checksum",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Arquivo gerado: {OUT}")
    print(f"Python: {platform.python_version()}")
    print(f"NumPy: {np.__version__}")
    print("Repetições válidas por tamanho: 30")
    print("Warm-ups descartados por tamanho: 5")


if __name__ == "__main__":
    main()
