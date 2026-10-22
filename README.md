# Dice Roll Simulator & Probability Checker

## 📌 Academic Disclosure & Project Timeline
*   **Project Development Period:** August 2024 – September 2024
*   **Primary Technologies:** Python 3.10+, NumPy, Matplotlib
*   **Repository Migration Note:** This project was originally developed, tested, and executed locally in mid-2024 as part of an academic and foundational study in statistical simulation. It was migrated and uploaded to GitHub in 2026 for digital portfolio consolidation, compilation, and academic review. 

---

An end-to-end beginner Python project exploring the **law of large numbers** using a fair six-sided die, NumPy, and Matplotlib.

## Objective
Simulate **10, 1,000, and 100,000 rolls**, count each face, and compare observed relative frequencies with the theoretical probability **1/6 ≈ 16.67%**.

**Important:** Larger samples tend to produce frequencies closer to 1/6, but do not guarantee exactly equal frequencies or improvement at every checkpoint. The law of large numbers is a mathematical theorem; this project illustrates it rather than proving it. It does not make individual rolls predictable.

## Quick Start
Requires Python 3.10 or newer. Run commands from this project directory.


## Files
- `simulator.py`: reusable simulation, chart generation, and command-line interface.
- `test_simulator.py`: validation, reproducibility, counting, and output tests.
- `requirements.txt`: dependency version ranges.
- `probability_comparison.png`: three bar charts with a common vertical scale.
- `convergence.png`: cumulative frequency trajectories on a logarithmic sample-size axis.
- `frequencies.csv`: 18 rows of face-level counts, probabilities, and errors.
- `RESULTS.md`: interpretation of the bundled experiment.

## Method
1. Create a NumPy generator with `np.random.default_rng(seed)`.
2. Draw uniformly distributed integers from 1 through 6 using `rng.integers(1, 7)`.
3. Use the first 10, 1,000, and 100,000 rolls of the same sequence.
4. Count outcomes with `np.bincount` and divide by the number of rolls.
5. Plot observed percentages against the theoretical reference line.

For face k, estimated probability = count(k) / number of rolls.
Absolute error = |estimated probability − 1/6|.

## What You Learn
- Discrete uniform distributions and relative frequencies.
- Seeded pseudorandom generation with NumPy.
- Vectorized counting and cumulative sums.
- Comparable Matplotlib bar charts and convergence plots.
- CSV exports, command-line arguments, and automated tests.
