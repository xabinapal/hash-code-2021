# Google Hash Code 2021 Qualification Phase

## Scores

### Dummy solution

Initial simple version with a one-second-cycle in every street.

```shell
./run_simulator.sh dummy [dataset].txt
./run_submitter.sh dummy
```

| Input Data Set     | Score     |
|--------------------|-----------|
| A - An example     | 1,001     |
| B - By the ocean   | 4,565,642 |
| C - Checkmate      | 1,231,878 |
| D - Daily conmute  | 969,685   |
| E - Etoile         | 661,797   |
| F - Forever jammed | 455,737   |
| **TOTAL**          | 7,885,740 |

### Optimized dummy solution

This variant checks if at least one car drives through an street and only keeps those streets.

```shell
./run_simulator.sh optimize dummy [dataset].txt
./run_submitter.sh optimize dummy
```

| Input Data Set     | Score     |
|--------------------|-----------|
| A - An example     | 1,001     |
| B - By the ocean   | 4,566,384 |
| C - Checkmate      | 1,298,723 |
| D - Daily conmute  | 1,571,622 |
| E - Etoile         | 680,987   |
| F - Forever jammed | 806,897   |
| **TOTAL**          | 8,925,614 |