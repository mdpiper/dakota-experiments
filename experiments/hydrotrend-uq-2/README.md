# HydroTrend UQ 2

This is an uncertainty quantification (UQ) experiment
with HydroTrend.

Stochastic expansion method.

Meant to be similiar to UQ-1,
but use polynomial chaos expansions (PCE)
instead of sampling.

LHS is still used.

Third-order polynomial in T.
Use only second-order polynomial in P dimension.

A total of 3 x 2 = 6 HydroTrend simulations are run.
From the results,
construct a polynomial fit to the _Qs hypersurface.
Then, iterate 10000 times over the hypersurface
to get statistics.



---

The input parameters `T` and `P`
are again used.
In this case, though,
we don't know their exact values,
so we set ranges&mdash;approximately &plusmn;10%
of their default values in WMT&mdash;and allow
`T` and `P` to vary uniformly over this range.
Latin Hypercube sampling (LHS)
is used to obtain 24 samples
from the `T-P` parameter space.
Dakota propagates these samples through the model,
and their effect on three output variables:

1. water discharge at the river mouth, `Q`,
1. long-term suspended sediment load at the river mouth, `Qs`, and
1. daily bedload at the river mouth, `Qb`,

is evaluated.

The experiment response functions
are the _median_ values
of the `Q`, `Qs`, and `Qb` series
over the 100-year duration of each HydroTrend run;
they're denoted by `_Q`, `_Qs`, and `_Qb`.
Dakota computes moments and 95% confidence intervals
for the response functions,
giving a measure of the spread of these variables
from the uncertainty in the input parameters.
The `response_levels` keyword is set
to a list of values for `_Q`, `_Qs`, and `_Qb`
at which histograms and CDFs are calculated.
Dakota also calculates several correlation matrices
between the model inputs and responses
(e.g., in this experiment, `_Q` is 99.8% correlated with `P`,
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

Be sure to view the statistics listed at the end of the 
**dakota.out** file.
