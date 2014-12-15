# HydroTrend DACE 1

This is a design and analysis of computer experiments (DACE) experiment
with HydroTrend.

The advantage of DACE
is that it decreases the number of model iterations
needed to approximate a set of desired model response functions
when compared to a multidimensional gridded parameter study.
Although this not as important for HydroTrend,
which runs quickly,
it will be important for models with a longer execution time.

In this experiment,
the same input parameters (`T`, `P`)
and response functions (`Qs_mean`, `Qs_stdev`)
from the **hydrotrend-ps-2** experiment
are used.
The Latin Hypercube sampling (LHS) technique
is used to obtain `N_s = 120` input points
from the `T-P` parameter space.
When used for DACE,
LHS divides each dimension of the parameter space
into `N_s` uniform partitions between the variable bounds.
Samples are then selected
such that every row and column in the hypercube of partitions
contains exactly one sample.
The resulting LHS sample set
has better coverage and less clustering
than Monte Carlo sampling.

For comparison with the output from **hydrotrend-ps-2**,
the results from this experiment
are interpolated to a rectangular grid.

Run this experiment with:

```bash
$ dakota -i dakota.in -o dakota.out &> run.log
```

## Notes

* The value of `N_s` was chosen to be one tenth the number of points
  used in the 40 x 30 gridded parameter study used in the
  **hydrotrend-ps-2** experiment.
* Set ranges of `T` and `P` to avoid NaN returns,
  which give scipy.interpolate.griddata difficulties.
* A seed value of 5 was chosen. The same seed should give same output.
