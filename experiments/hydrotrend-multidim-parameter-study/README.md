# HydroTrend Multidim Parameter Study Experiment

In this computer experiment,
a two-dimensional parameter study of HydroTrend
is performed with Dakota.

The default parameter values defined for HydroTrend in WMT,
in the files
<a href="./HYDRO_IN/HYDRO.IN">HYDRO.IN</a>
and
<a href="./HYDRO_IN/HYDRO0.HYPS">HYDRO0.HYPS</a>,
are used as a starting point.
Two HydroTrend parameters,
_starting mean annual temperature_ (#8, here `T`, in Celsius) and
_starting mean annual precipitation_ (#9, here `P`, in m),
are perturbed
to determine their effects on
_long-term suspended sediment load_, `Qs`,
over 36500 days of simulation time.

Given lower and upper bounds on the values of `T` and `P`,
the parameter space is partitioned into
five equal intervals in each dimension,
forming a grid.
A HydroTrend simulation is performed
for the parameter values at each node of the grid,
for a total of 36 runs.
For each run,
the mean and standard deviation of the resulting `Qs` series
are calculated.

Run this experiment with:

```bash
$ dakota -i dakota-hydrotrend-2.in -o dakota-hydrotrend-2.out &> run.log
```

Instructions are given to Dakota through the input file
<a href="./dakota-hydrotrend-2.in">dakota-hydrotrend-2.in</a>.
Dakota calls the executable Python script
<a href="./run_hydrotrend.py">run_hydrotrend.py</a>,
which acts as a broker between Dakota and HydroTrend,
with communication 
through temporary files on the filesystem.
Output from Dakota is captured in
**dakota-hydrotrend-2.out**.
Tabular results of the experiment
are stored in
**dakota-hydrotrend-2.dat**.
Messages from stdout and stderr are filed in
**run.log**.
Clean up intermediate results with the shell script
<a href="./dakota_cleanup">dakota_cleanup</a>.

## Notes

* Two response functions are used for the mean and standard deviation
  of the `Qs` series.
* The bounds on `T` and `P` were chosen to be
  close to the default values used in WMT.
* HydroTrend automatically updates the monthly mean climate variables
  (#12-23), based on the values of `T` and `P`. However, the standard
  deviations are not altered.
* The minimum value of `P` must be greater than the value of _constant
  annual base flow_, parameter #11.
* HydroTrend gives warnings that there is snow remaining on Aug 31 for
  `T` <= 12.
