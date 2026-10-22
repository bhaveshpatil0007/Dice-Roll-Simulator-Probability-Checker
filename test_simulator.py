"""Run with: python -m unittest discover -v"""
import unittest
from tempfile import TemporaryDirectory
from pathlib import Path
import numpy as np
from simulator import simulate, save_results

class SimulatorTests(unittest.TestCase):
    def test_range_counts_and_probabilities(self):
        rolls, results = simulate()
        self.assertEqual(len(rolls), 100000)
        self.assertTrue(np.all((rolls >= 1) & (rolls <= 6)))
        for result in results:
            self.assertEqual(int(result["counts"].sum()), result["n"])
            self.assertAlmostEqual(float(result["probabilities"].sum()), 1)
            np.testing.assert_array_equal(result["counts"], np.bincount(rolls[:result["n"]], minlength=7)[1:])

    def test_reproducibility(self):
        np.testing.assert_array_equal(simulate(seed=7)[0], simulate(seed=7)[0])

    def test_invalid_sizes(self):
        for sizes in [[], [0], [-1], [2.5]]:
            with self.assertRaises(ValueError):
                simulate(sizes)

    def test_output_files(self):
        rolls, results = simulate([10, 100])
        with TemporaryDirectory() as directory:
            save_results(rolls, results, directory)
            for name in ["frequencies.csv", "probability_comparison.png", "convergence.png"]:
                self.assertGreater((Path(directory) / name).stat().st_size, 0)

if __name__ == "__main__":
    unittest.main()
