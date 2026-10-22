# Dice Roll Simulator & Probability Checker

An end-to-end beginner Python project exploring the **law of large numbers** using a fair six-sided die, NumPy, and Matplotlib.

## Objective
Simulate **10, 1,000, and 100,000 rolls**, count each face, and compare observed relative frequencies with the theoretical probability **1/6 ≈ 16.67%**.

**Important:** Larger samples tend to produce frequencies closer to 1/6, but do not guarantee exactly equal frequencies or improvement at every checkpoint. The law of large numbers is a mathematical theorem; this project illustrates it rather than proving it. It does not make individual rolls predictable.

## Quick start
Requires Python 3.10 or newer. Run commands from this project directory.

```bash
python -m venv .venv
```
Activate your environment:
- Windows: `.venv\Scripts\activate`
- macOS/Linux: `source .venv/bin/activate`

```bash
python -m pip install -r requirements.txt
python simulator.py
python -m unittest discover -v
```

## Custom runs
```bash
python simulator.py --seed 123 --rolls 10 1000 100000 --output custom_outputs
```
A fixed seed makes the pseudorandom experiment reproducible within the same software environment. Included sample outputs were generated with seed 42. This is an educational simulator, not a security-grade random generator.

## Files
- `simulator.py`: reusable simulation, chart generation, and command-line interface.
- `test_simulator.py`: validation, reproducibility, counting, and output tests.
- `requirements.txt`: dependency version ranges.
- `probability_comparison.png`: three bar charts with a common vertical scale.
- `convergence.png`: cumulative frequency trajectories on a logarithmic sample-size axis.
- `frequencies.csv`: 18 rows of face-level counts, probabilities, and errors.
- `RESULTS.md`: interpretation of the bundled experiment.
- `sample_run.txt`: console output from the bundled run.

## Method
1. Create a NumPy generator with `np.random.default_rng(seed)`.
2. Draw uniformly distributed integers from 1 through 6 using `rng.integers(1, 7)` (upper bound excluded).
3. Use the first 10, 1,000, and 100,000 rolls of the same sequence. These are nested checkpoints, not independent experiments.
4. Count outcomes with `np.bincount` and divide by the number of rolls.
5. Plot observed percentages against the theoretical reference line.
6. Export a CSV and inspect maximum absolute deviations.

For face k, estimated probability = count(k) / number of rolls.
Absolute error = |estimated probability − 1/6|.
Multiply an error by 100 to express it in percentage points.

## Probability checker: scope
The checker reports descriptive deviations from a known fair-die probability. It is **not** a formal hypothesis test for whether a physical die is fair. Rolls are modeled as independent and identically distributed. Real dice may violate this assumption.

## What you learn
- Discrete uniform distributions and relative frequencies.
- Seeded pseudorandom generation with NumPy.
- Vectorized counting and cumulative sums.
- Comparable Matplotlib bar charts and convergence plots.
- CSV exports, command-line arguments, and automated tests.

## Upload / submission
Upload the entire unzipped project folder to your repository or submit the ZIP. The generated outputs are included so the project can be reviewed before installation. For GitHub, create an empty repository, then run inside this folder:

```bash
git init
git add .
git commit -m "Add dice probability simulation project"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```
Replace `YOUR_REPOSITORY_URL` with your own repository address. No credentials or external data are required to run this project.

## Extensions
Try multiple seeds; add a biased die; compare different numbers of sides; or investigate how typical estimation error scales with sample size. Avoid interpreting one sample path as a guarantee of monotonic convergence.

## Displaying the graphs
Running `python simulator.py` now opens both Matplotlib figures by default.
Close the graph windows to let the program finish. Charts and the CSV are also
saved alongside the script, regardless of your terminal's working directory.
All project files are in this single folder; there is no outputs subfolder.

For a server or environment without a graphical display, use:
```bash
python simulator.py --no-show
```
Then open the included PNG images directly. Interactive windows require a local
Python environment with a working graphical Matplotlib backend; headless online
runners cannot open desktop windows.
