# Dakota: HydroTrend Centered Parameter Study Experiment

In this computer experiment,
a centered parameter study of HydroTrend
is performed with Dakota.

The default parameter values defined for HydroTrend in WMT,
in the files
<a href="./HYDRO_IN/HYDRO.IN">HYDRO.IN</a>
and
<a href="./HYDRO_IN/HYDRO0.HYPS">HYDRO0.HYPS</a>,
are used as a starting point.
Two HydroTrend parameters,
_river basin length_ (#28, here `L_r`, in km)
and _drainage area of reservoirs_ (#29, here `W`, in km^2),
are perturbed
to see their effects on
long-term suspended sediment load
(here `Qsbar`, in kg/s).
The initial values of `L_r` and `W`
are used as the center point in parameter space.
This center point,
as well as two steps from the center
in each direction in parameter space,
are evaluated,
for a total of nine `Qsbar` values computed by HydroTrend.

<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="100" height="100">
  <path d=" M 50 28
			L 50 32
			M 50 38
			L 50 42
			M 50 48
			L 50 52
			M 50 58
			L 50 62
			M 50 68
			L 50 72
			M 28 50
			L 32 50
			M 38 50
			L 42 50
			M 58 50
			L 62 50
			M 68 50
			L 72 50"
            stroke="red" stroke-width="4" fill="none" />
</svg>

Run this experiment with:

	$ dakota -i dakota-hydrotrend-1.in -o dakota-hydrotrend-1.out &> run.log

Instructions are given to Dakota through the input file
<a href="./dakota-hydrotrend-1.in">dakota-hydrotrend-1.in</a>.
Dakota calls the shell script
<a href="./run_hydrotrend">run_hydrotrend</a>,
which acts as a broker between Dakota and HydroTrend,
with communication 
through temporary files on the filesystem.
Output from Dakota is captured in
<a href="./dakota-hydrotrend-1.out">dakota-hydrotrend-1.out</a>.
Tabular results of the experiment
are stored in
<a href="./dakota-hydrotrend-1.dat">dakota-hydrotrend-1.dat</a>.
Messages from stdout and stderr are filed in
<a href="./run.log">run.log</a>.

Clean up intermediate results with the script
<a href="./dakota_cleanup">dakota_cleanup</a>.
