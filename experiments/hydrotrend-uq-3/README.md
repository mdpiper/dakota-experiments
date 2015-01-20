# HydroTrend UQ 3

This is an uncertainty quantification (UQ) experiment
with HydroTrend.

This experiment uses
a stochastic collocation technique
similar to the PCE technique
used in **hydrotrend-uq-2**,
and with nearly identical settings.
The significant departure from the former experiment is
the input parameters `T` and `P`
are expressed as normally distributed random variables,
with means and standard deviations
taken from the defaults in WMT.

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

These are the statistics listed at the end of the 
**dakota.out** file.

```
Statistics derived analytically from polynomial expansion:

Moment-based statistics for each response function:
                            Mean           Std Dev          Skewness          Kurtosis
_Qs
  expansion:    4.0159166667e+00  4.6718379829e-01  1.9278779773e-01 -7.1263593116e-01
  integration:  4.0159166667e+00  4.6718379829e-01  1.9278779773e-01 -7.1263593116e-01

Covariance matrix for response functions:
[[  2.1826070139e-01 ]] 

Local sensitivities for each response function evaluated at uncertain variable means:
_Qs:
 [  3.5488046242e-01  2.1872770582e+00 ] 

Global sensitivity indices for each response function:
_Qs Sobol' indices:
                                  Main             Total
                      3.7764573145e-01  3.8065452499e-01 T
                      6.1934547501e-01  6.2235426855e-01 P
                           Interaction
                      3.0087935423e-03 T P 

Statistics based on 10000 samples performed on polynomial expansion:

Probability Density Function (PDF) histograms for each response function:
PDF for _Qs:
          Bin Lower          Bin Upper      Density Value
          ---------          ---------      -------------
   2.3634125667e+00   3.0000000000e+00   1.7122549756e-02
   3.0000000000e+00   3.5000000000e+00   2.3460000000e-01
   3.5000000000e+00   4.0000000000e+00   7.4400000000e-01
   4.0000000000e+00   4.5000000000e+00   6.9880000000e-01
   4.5000000000e+00   5.0000000000e+00   2.6060000000e-01
   5.0000000000e+00   6.4881264355e+00   1.3506916832e-02

Level mappings for each response function:
Cumulative Distribution Function (CDF) for _Qs:
     Response Level  Probability Level  Reliability Index  General Rel Index
     --------------  -----------------  -----------------  -----------------
   3.0000000000e+00   1.0900000000e-02
   3.5000000000e+00   1.2820000000e-01
   4.0000000000e+00   5.0020000000e-01
   4.5000000000e+00   8.4960000000e-01
   5.0000000000e+00   9.7990000000e-01
```
