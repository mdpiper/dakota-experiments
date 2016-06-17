# Delft3D Polynomial Chaos Experiment 1

This is an uncertainty quantification (UQ) experiment
with [Delft3D](http://oss.deltares.nl/web/delft3d).

In this experiment,
the polynomial chaos expansion (PCE) technique 
(see also **hydrotrend-polynomial-chaos**)
is used
to measure the effects of varying three parameters:

* sand diameter (`Sand-SedDia`),
* silt diameter (`Silt-SedDia`), and
* critical shear stress of erosion (`Mud-TcrEro`)

on three model responses:

* total sedimentation (`TotalSed`),
* total accretion (`TotalAgr`), and
* total erosion (`TotalEro`).

A third-order PCE is chosen.
Latin Hypercube sampling
is used to select three values for each parameter
from their distribution.
Therefore,
the number of model runs is:

    n_values^n_parameters = 3^3 = 27

Two calls to Dakota are required to run this experiment;
one to set up the Delft3D runs on ***beach***,
the other to analyze the results.
Details are given below.

## Files

This table describes the files used in this experiment.

| File | Purpose |
| ---- | ------- |
| **delft3d_run.in** | Dakota input file that submits Delft3D jobs to queue. |
| **delft3d_run.py** | Analysis driver for **delft3d_run.in**. |
| **delft3d_analyze.in** | Dakota input file that calls **total_sed_cal.m** to analysze the results of each Delft3D run. |
| **delft3d_analyze.py** | Analysis driver for **delft3d_analysis.in**. |
| **WLD.sed.template** | A template for the Delft3D input file, containing sediment parameters that will be varied. |
| **fake.out** | A Dakota results file containing dummy values, used to advance Dakota after submitting a Delft3D run. |
| **total_sed_cal.m** | A MATLAB program used to calculate the response statistics from Delft3D output. |
| **nesting.txt** | A two-column text file that lists the output cells used in the analysis of the results. |

## Execution

This experiment requires two calls to Dakota.
The first call uses **delft3d_run.in** to submit
the series of Delft3D jobs to the queue manager:
```bash
$ dakota -i delft3d_run.in &> delft3d_run.log &
```
The Dakota process exits fairly quickly,
but the Delft3D runs take much longer;
monitor the queue to see when they're complete.
The analysis driver also copies the file **fake.out**
to the run directory
so Dakota will advance.
No statistics are calculated in this first call!

When all of the Delft3D runs are finished,
call Dakota again with **delft3d_analyze.in** to analyze the results:
```bash
$ dakota -i delft3d_analyze.in -o dakota.out
```
The analysis driver
calls the MATLAB script in **total_sed_cal.m**
to calculate `TotalSed`, `TotalAgr`, and `TotalEro`,
then write the results to the "real" Dakota results file.
The tabular data file **dakota.dat**,
containing the Delft3D input and output values,
and the Dakota output file **dakota.out**,
containing the results of the UQ,
are returned in this step.

Note that the second Dakota call
can't be backgrounded -- the Delft3D-MATLAB
library function used in **total_sed_cal.m** will hang,
terminating the process with no error message.

## Results

These are the experimental results listed at the end
of the **dakota.out** file.

```
Statistics derived analytically from polynomial expansion:

Moment-based statistics for each response function:
                            Mean           Std Dev          Skewness          Kurtosis
TotalSed
  expansion:   -5.2830545968e+05  2.6826441806e+05
  integration: -5.2830545968e+05  2.6826441806e+05 -8.5925107448e-01 -1.0075618522e+00
TotalAgr
  expansion:    2.4392075893e+05  3.3292669381e+04
  integration:  2.4392075893e+05  3.3292669381e+04 -4.8996752085e-01 -2.2798363626e-01
TotalEro
  expansion:   -7.7800651468e+05  2.4812224435e+05
  integration: -7.7800651468e+05  2.4812224435e+05 -8.5687959979e-01 -9.5212979480e-01

Covariance matrix for response functions:
[[  7.1965797999e+10  6.2041133644e+09  6.6249467372e+10
    6.2041133644e+09  1.1084018345e+09  5.1358149316e+09
    6.6249467372e+10  5.1358149316e+09  6.1564648143e+10 ]]

Local sensitivities for each response function evaluated at uncertain variable means:
TotalSed:
 [  1.2460638891e+09  1.5588011210e+09  9.4535941750e+05 ]
TotalAgr:
 [ -8.5222434821e+08  7.2909106023e+08  8.8456407555e+04 ]
TotalEro:
 [  2.1079209887e+09  8.3595768106e+08  8.6332725631e+05 ]

Global sensitivity indices for each response function:
TotalSed Sobol' indices:
                                  Main             Total
                      8.7796560208e-03  8.9639735088e-03 Sand-SedDia
                      7.9067173720e-03  7.9514520140e-03 Silt-SedDia
                      9.8308534162e-01  9.8331288216e-01 Mud-TcrEro
                           Interaction
                      7.4444711129e-07 Sand-SedDia Silt-SedDia
                      1.8355034652e-04 Sand-SedDia Mud-TcrEro
                      4.3967500570e-05 Silt-SedDia Mud-TcrEro
                      2.2694312350e-08 Sand-SedDia Silt-SedDia Mud-TcrEro
TotalAgr Sobol' indices:
                                  Main             Total
                      3.6322430374e-01  3.6346319655e-01 Sand-SedDia
                      1.1269506209e-01  1.1412215716e-01 Silt-SedDia
                      5.2244956940e-01  5.2405529571e-01 Mud-TcrEro
                           Interaction
                      2.5338462380e-05 Sand-SedDia Silt-SedDia
                      2.0396970466e-04 Sand-SedDia Mud-TcrEro
                      1.3921719505e-03 Silt-SedDia Mud-TcrEro
                      9.5846523776e-06 Sand-SedDia Silt-SedDia Mud-TcrEro
TotalEro Sobol' indices:
                                  Main             Total
                      3.1015098591e-02  3.1271894710e-02 Sand-SedDia
                      2.7165836100e-03  2.8672080673e-03 Silt-SedDia
                      9.6586271050e-01  9.6626658127e-01 Mud-TcrEro
                           Interaction
                      1.7365291913e-06 Sand-SedDia Silt-SedDia
                      2.5498283912e-04 Sand-SedDia Mud-TcrEro
                      1.4881117768e-04 Silt-SedDia Mud-TcrEro
                      7.6750419321e-08 Sand-SedDia Silt-SedDia Mud-TcrEro

Statistics based on 10000 samples performed on polynomial expansion:

Probability Density Function (PDF) histograms for each response function:
PDF for TotalSed:
          Bin Lower          Bin Upper      Density Value
          ---------          ---------      -------------
  -1.2877057356e+06  -1.0000000000e+06   3.0343503512e-07
  -1.0000000000e+06  -8.0000000000e+05   5.4400000000e-07
  -8.0000000000e+05  -6.0000000000e+05   6.6050000000e-07
  -6.0000000000e+05  -4.0000000000e+05   9.5700000000e-07
  -4.0000000000e+05  -2.0000000000e+05   2.4020000000e-06
PDF for TotalAgr:
          Bin Lower          Bin Upper      Density Value
          ---------          ---------      -------------
   9.6872781066e+04   1.0000000000e+05   9.5931882721e-08
   1.0000000000e+05   1.5000000000e+05   1.3600000000e-07
   1.5000000000e+05   2.0000000000e+05   2.0180000000e-06
   2.0000000000e+05   2.5000000000e+05   8.2260000000e-06
   2.5000000000e+05   3.0000000000e+05   9.1400000000e-06
   3.0000000000e+05   3.1605652084e+05   1.4760358256e-06
PDF for TotalEro:
          Bin Lower          Bin Upper      Density Value
          ---------          ---------      -------------
  -1.5061480282e+06  -1.2000000000e+06   2.9822174767e-07
  -1.2000000000e+06  -1.0000000000e+06   6.0300000000e-07
  -1.0000000000e+06  -8.0000000000e+05   7.7750000000e-07
  -8.0000000000e+05  -6.0000000000e+05   1.5685000000e-06
  -6.0000000000e+05  -4.0000000000e+05   1.5945000000e-06

Level mappings for each response function:
Cumulative Distribution Function (CDF) for TotalSed:
     Response Level  Probability Level  Reliability Index  General Rel Index
     --------------  -----------------  -----------------  -----------------
  -1.0000000000e+06   8.7300000000e-02
  -8.0000000000e+05   1.9610000000e-01
  -6.0000000000e+05   3.2820000000e-01
  -4.0000000000e+05   5.1960000000e-01
  -2.0000000000e+05   1.0000000000e+00
Cumulative Distribution Function (CDF) for TotalAgr:
     Response Level  Probability Level  Reliability Index  General Rel Index
     --------------  -----------------  -----------------  -----------------
   1.0000000000e+05   3.0000000000e-04
   1.5000000000e+05   7.1000000000e-03
   2.0000000000e+05   1.0800000000e-01
   2.5000000000e+05   5.1930000000e-01
   3.0000000000e+05   9.7630000000e-01
Cumulative Distribution Function (CDF) for TotalEro:
     Response Level  Probability Level  Reliability Index  General Rel Index
     --------------  -----------------  -----------------  -----------------
  -1.2000000000e+06   9.1300000000e-02
  -1.0000000000e+06   2.1190000000e-01
  -8.0000000000e+05   3.6740000000e-01
  -6.0000000000e+05   6.8110000000e-01
  -4.0000000000e+05   1.0000000000e+00
```
