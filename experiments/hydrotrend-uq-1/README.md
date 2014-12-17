# HydroTrend UQ 1

This is an uncertainty quantification (UQ) experiment
with HydroTrend.

As in other HydroTrend experiments,
the input parameters `T` and `P`
are used,
although, in this case, over a much smaller,
and more physical,
range of values.
Instead of examining
long-term suspended sediment load at the river mouth, `Qs`,
used in earlier experiments,
the effect of varying `T` and `P`
on water discharge at the river mouth, `Q`,
is evaluated.
The experiment response functions are the mean and standard deviation
of the cumulative discharge over the 100-year simulation,
`Q_mean` and `Q_stdev`.

Latin Hypercube sampling (LHS)
is used to obtain `N_s = 20` input points
from the `T-P` parameter space.

By specifying the `asynchronous` keyword
in the Dakota input file,
runs are performed in parallel,
using two (the number of processors on my Mac)
concurrent evaluations.

For comparison with the output
from **hydrotrend-ps-2** and **hydrotrend-dace-1**,
the results from this experiment
are interpolated to a rectangular grid.

Run this experiment with:

```bash
$ dakota -i dakota.in -o dakota.out &> run.log
```

## Notes

* The value of `N_s` was chosen to be a tiny fraction of the number of
  points used in the 40 x 30 gridded parameter study in
  **hydrotrend-ps-2**.
* A seed value of 17 was chosen to obtain repeatable results over
  multiple runs.
