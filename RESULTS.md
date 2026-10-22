# Results: seeded example

Seed: **42**. Each checkpoint uses a prefix of the same simulated sequence.

| Rolls | Maximum absolute error (percentage points) |
|---:|---:|
| 10 | 13.3333 |
| 1,000 | 1.5333 |
| 100,000 | 0.1463 |

In this run, the largest checkpoint is closer to the theoretical distribution than the smallest checkpoint. This illustrates the law of large numbers, but does not establish that errors decrease at every step or for every seed. The reference probability is exactly 1/6, approximately 16.67%, not exactly 16.6%.

All four automated tests passed when the bundled outputs were generated.
