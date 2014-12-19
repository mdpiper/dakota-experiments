# HydroTrend UQ 1

This is an uncertainty quantification (UQ) experiment
with HydroTrend.

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
Here are the results of this experiment:

```
Statistics based on 24 samples:

Moment-based statistics for each response function:
                            Mean           Std Dev          Skewness          Kurtosis
            _Q  3.9329895833e+01  3.0661052266e+00  9.9102601075e-02 -1.2287970701e+00
           _Qs  4.1578541667e+00  4.7282402001e-01  1.3775599387e-01 -1.2626313738e+00
           _Qb  9.9814583333e-01  7.7807381896e-02  1.0036271003e-01 -1.2279684467e+00

95% confidence intervals for each response function:
                    LowerCI_Mean      UpperCI_Mean    LowerCI_StdDev    UpperCI_StdDev
            _Q  3.8035193145e+01  4.0624598522e+01  2.3830186442e+00  4.3010116436e+00
           _Qs  3.9581980933e+00  4.3575102400e+00  3.6748525307e-01  6.6325891160e-01
           _Qb  9.6529065744e-01  1.0310010092e+00  6.0472954454e-02  1.0914513063e-01

Level mappings for each response function:
Cumulative Distribution Function (CDF) for _Q:
     Response Level  Probability Level  Reliability Index  General Rel Index
     --------------  -----------------  -----------------  -----------------
   3.0000000000e+01   0.0000000000e+00
   3.5000000000e+01   8.3333333333e-02
   4.0000000000e+01   5.4166666667e-01
   4.5000000000e+01   1.0000000000e+00
   5.0000000000e+01   1.0000000000e+00
Cumulative Distribution Function (CDF) for _Qs:
     Response Level  Probability Level  Reliability Index  General Rel Index
     --------------  -----------------  -----------------  -----------------
   3.0000000000e+00   0.0000000000e+00
   3.5000000000e+00   4.1666666667e-02
   4.0000000000e+00   3.7500000000e-01
   4.5000000000e+00   7.0833333333e-01
   5.0000000000e+00   1.0000000000e+00
Cumulative Distribution Function (CDF) for _Qb:
     Response Level  Probability Level  Reliability Index  General Rel Index
     --------------  -----------------  -----------------  -----------------
   7.0000000000e-01   0.0000000000e+00
   8.0000000000e-01   0.0000000000e+00
   9.0000000000e-01   1.2500000000e-01
   1.0000000000e+00   5.0000000000e-01
   1.1000000000e+00   9.1666666667e-01

Probability Density Function (PDF) histograms for each response function:
PDF for _Q:
          Bin Lower          Bin Upper      Density Value
          ---------          ---------      -------------
   3.0000000000e+01   3.5000000000e+01   1.6666666667e-02
   3.5000000000e+01   4.0000000000e+01   9.1666666667e-02
   4.0000000000e+01   4.5000000000e+01   9.1666666667e-02
   4.5000000000e+01   5.0000000000e+01   0.0000000000e+00
PDF for _Qs:
          Bin Lower          Bin Upper      Density Value
          ---------          ---------      -------------
   3.0000000000e+00   3.5000000000e+00   8.3333333333e-02
   3.5000000000e+00   4.0000000000e+00   6.6666666667e-01
   4.0000000000e+00   4.5000000000e+00   6.6666666667e-01
   4.5000000000e+00   5.0000000000e+00   5.8333333333e-01
PDF for _Qb:
          Bin Lower          Bin Upper      Density Value
          ---------          ---------      -------------
   7.0000000000e-01   8.0000000000e-01   0.0000000000e+00
   8.0000000000e-01   9.0000000000e-01   1.2500000000e+00
   9.0000000000e-01   1.0000000000e+00   3.7500000000e+00
   1.0000000000e+00   1.1000000000e+00   4.1666666667e+00
   1.1000000000e+00   1.1270000000e+00   3.0864197531e+00

Simple Correlation Matrix among all inputs and outputs:
                        T            P           _Q          _Qs          _Qb 
           T  1.00000e+00 
           P  3.27442e-02  1.00000e+00 
          _Q  2.36371e-02  9.98306e-01  1.00000e+00 
         _Qs  9.68684e-01  2.24269e-01  2.13460e-01  1.00000e+00 
         _Qb  2.28413e-02  9.98257e-01  9.99994e-01  2.12642e-01  1.00000e+00 

Partial Correlation Matrix between input and output:
                       _Q          _Qs          _Qb 
           T -1.55636e-01  9.86998e-01 -1.66923e-01 
           P  9.98346e-01  7.75902e-01  9.98305e-01 

Simple Rank Correlation Matrix among all inputs and outputs:
                        T            P           _Q          _Qs          _Qb 
           T  1.00000e+00 
           P  4.00000e-02  1.00000e+00 
          _Q  4.95652e-02  9.99130e-01  1.00000e+00 
         _Qs  9.73913e-01  1.90435e-01  1.98261e-01  1.00000e+00 
         _Qb  4.95652e-02  9.99130e-01  1.00000e+00  1.98261e-01  1.00000e+00 

Partial Rank Correlation Matrix between input and output:
                       _Q          _Qs          _Qb 
           T  2.30434e-01  9.85097e-01  2.30434e-01 
           P  9.99175e-01  6.68071e-01  9.99175e-01 
```
