# HydroTrend UQ 2

This is an uncertainty quantification (UQ) experiment
with HydroTrend.

Unlike **hydrotrend-uq-1**,
which uses sampling to propagate uncertainties through a model,
this experiment uses 
polynomial chaos expansions (PCE),
a stochastic expansion method.
With this technique,
a polynomial fit to a response function is generated;
UQ statistics are
calculated from it
both analytically and by sampling.
Further,
estimates are made for the amount of uncertainty
in the response
than can be attributed to the input variables.

As in **hydrotrend-uq-1**,
the input parameters `T` and `P`
are used,
varying uniformly over an interval approximately
&plusmn;10%
of their default values in WMT.
The experiment response function
is the median value
of the `Qs` series
over the 100-year duration of a HydroTrend run;
it's denoted by `_Qs`.

A third-order polynomial fit for `_Qs` is requested.
However, by specifying the 
`dimension_preference` keyword,
only a second-order polynomial in the `P` dimension is used.
So,
only 3 x 2 = 6 HydroTrend simulations
are needed to construct the polynomial fit.
LHS is used to select the 6 points in `T-P` space
where HydroTrend is run.
A seed value is specified in order to obtain repeatable results
over multiple runs.

Dakota computes moments analytically
for the polynomial fit to the response function,
giving a measure of the spread of `Qs`
from the uncertainty in the input parameters.
(Note that this experiment uses 
a factor of four fewer HydroTrend runs than in **hydrotrend-uq-1**,
yet it achieves similar moments for `_Qs`.)
Because the `variance_based_decomp` keyword was set,
Dakota computes sensitivity indices,
which show which parameters have the most influence on the output.
In this experiment (see below),
the Sobol' main index for `T` at 0.92 is much larger
the the index for `P`
and the index for the interaction between `T` and `P`.
The sum of the main indices must be less than or equal to 1.0.

From the `_Qs` polynomial fit,
10000 samples are chosen
for calculating statistics.
The `response_levels` keyword
provides a list of values for `_Qs`
at which its PDF and CDF are calculated.
From this experiment,
the probability that `_Qs` is less than 4.5
over the uncertain values of `T` and `P` is 0.75.


## Execution

Run this experiment with:

```bash
$ dakota -i dakota.in -o dakota.out &> run.log
```

or with the **dakota_utils** package script `dakota_run`:

```bash
$ dakota_run .
```

## Results

Be sure to view the statistics listed at the end of the 
**dakota.out** file.

```
Statistics derived analytically from polynomial expansion:

Moment-based statistics for each response function:
                            Mean           Std Dev          Skewness          Kurtosis
_Qs
  expansion:    4.1149444444e+00  4.7941203541e-01
  integration:  4.1149444444e+00  4.7941203541e-01  1.2148683172e-01 -1.0262089453e+00

Covariance matrix for response functions:
[[  2.2983589969e-01 ]] 

Local sensitivities for each response function evaluated at uncertain variable means:
_Qs:
 [  5.3124421565e-01  1.1604740411e+00 ] 

Global sensitivity indices for each response function:
_Qs Sobol' indices:
                                  Main             Total
                      9.2194041115e-01  9.2268235221e-01 T
                      7.7317647791e-02  7.8059588852e-02 P
                           Interaction
                      7.4194106137e-04 T P 

Statistics based on 10000 samples performed on polynomial expansion:

Probability Density Function (PDF) histograms for each response function:
PDF for _Qs:
          Bin Lower          Bin Upper      Density Value
          ---------          ---------      -------------
   3.0000000000e+00   3.5000000000e+00   2.1500000000e-01
   3.5000000000e+00   4.0000000000e+00   6.7220000000e-01
   4.0000000000e+00   4.5000000000e+00   6.0380000000e-01
   4.5000000000e+00   5.0000000000e+00   4.6500000000e-01
   5.0000000000e+00   5.2091494458e+00   1.0518794306e-01

Level mappings for each response function:
Cumulative Distribution Function (CDF) for _Qs:
     Response Level  Probability Level  Reliability Index  General Rel Index
     --------------  -----------------  -----------------  -----------------
   3.0000000000e+00   0.0000000000e+00
   3.5000000000e+00   1.0750000000e-01
   4.0000000000e+00   4.4360000000e-01
   4.5000000000e+00   7.4550000000e-01
   5.0000000000e+00   9.7800000000e-01
```
