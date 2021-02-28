# Google Hash Code 2021 Qualification Phase

## Best scores

| Input Data Set     | Score         | Solution              |
|--------------------|---------------|-----------------------|
| A - An example     |       2,002   | Congestion (factor 1) |
| B - By the ocean   |   4,567,121   | Congestion (factor 2) |
| C - Checkmate      |   1,231,878   | Dummy                 |
| D - Daily conmute  |   1,588,367   | Congestion (factor 3) |
| E - Etoile         |     721,371   | Congestion (factor 1) |
| F - Forever jammed |   1,341,925   | Congestion (factor 1) |
| **TOTAL**          | **9,452,664** |                       |

## Solutions

### Dummy solution

Initial simple version with a one-second-cycle in every street.

```shell
./run_simulator.sh dummy [dataset].txt
./run_submitter.sh dummy
```

| Input Data Set     | Score         |
|--------------------|---------------|
| A - An example     |       1,001   |
| B - By the ocean   |   4,565,642   |
| C - Checkmate      | **1,231,878** |
| D - Daily conmute  |     969,685   |
| E - Etoile         |     661,797   |
| F - Forever jammed |     455,737   |
| **TOTAL**          | **7,885,740** |

### Optimized dummy solution

This variant checks if at least one car drives through an street and only keeps those streets.

```shell
./run_simulator.sh optimize dummy [dataset].txt
./run_submitter.sh optimize dummy
```

| Input Data Set     | Score         |
|--------------------|---------------|
| A - An example     |       1,001   |
| B - By the ocean   |   4,566,384   |
| C - Checkmate      |   1,298,723   |
| D - Daily conmute  | **1,571,622** |
| E - Etoile         |     680,987   |
| F - Forever jammed |     806,897   |
| **TOTAL**          | **8,925,614** |

### Street congestion solution

This scenario takes into account cars driving through streets and number of streets entering each intersection to assign proportional traffic light time.

```shell
CONGESTION_FACTOR=[factor] ./run_simulator.sh optimize congestion [dataset].txt
CONGESTION_FACTOR=[factor] ./run_submitter.sh optimize congestion
```

| Input Data Set     | Score (factor 1) | Score (factor 2) | Score (factor 3) |
|--------------------|------------------|------------------|------------------|
| A - An example     |     **2,002**    |     **2,002**    |     **2,002**    |
| B - By the ocean   |   4,566,874      | **4,567,121**    |   4,566,872      |
| C - Checkmate      | **1,299,766**    |   1,299,054      |   1,298,872      |
| D - Daily conmute  |     349,905      |   1,473,151      | **1,588,367**    |
| E - Etoile         |   **721,371**    |     706,739      |     702,116      |
| F - Forever jammed | **1,341,925**    |   1,247,728      |   1,119,669      |
| **TOTAL**          |   8,281,843      | **9,313,817**    |   9,277,898      |