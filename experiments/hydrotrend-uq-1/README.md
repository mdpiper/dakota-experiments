# HydroTrend UQ 1

This is an uncertainty quantification (UQ) experiment
with HydroTrend.

The input parameters `T` and `P`
are again used.
In this case, though,
we don't know their exact values,
so we set a range of values&mdash;approximately &plusmn;10%
of the default values used in WMT&mdash;and allow
`T` and `P` to vary uniformly over this range.
Latin Hypercube sampling (LHS)
is used to obtain 24 input points
from the `T-P` parameter space.
Dakota propagates these samples through the model,
and the effect
on water discharge at the river mouth, `Q`,
is evaluated.

The experiment response functions are the mean and standard deviation
of the cumulative `Q` over the 100-year simulation,
`Q_mean` and `Q_stdev`.
Dakota computes moments and 95% confidence intervals
for the response functions,
giving a measure of the spread of `Q_mean` and `Q_stdev`
from the uncertainty in the input parameters.
The `response_levels` keyword is set
to a list of values for `Q_mean` and `Q_stdev`
at which histograms and CDFs are calculated.
Dakota also calculates various correlation matrices
between the model inputs and responses
(e.g., in this experiment, `Q_mean` is 100% correlated with `P`,
and vanishingly correlated with `T`).
A seed value is specified in order to obtain repeatable results
over multiple runs.

By setting the `asynchronous` keyword
in the Dakota input file,
runs are performed in parallel,
using two (the number of processors on my Mac)
concurrent evaluations.

Run this experiment with:

```bash
$ dakota -i dakota.in -o dakota.out &> run.log
```

or with the **dakota_utils** package script `dakota_run`:

```bash
$ dakota_run .
```

Be sure to check out the statistics listed at the end of the 
**dakota.out** file.
