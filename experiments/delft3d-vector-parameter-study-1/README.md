# Delft3D Vector Parameter Study 1

This is a vector parameter study experiment with Delft3D.

## Files

| File | Purpose |
| ---- | ------- |
| **WLD.sed.template** | The Delft3D input file, containing parameter values that will be perturbed. |
| **nesting.txt** | A two-column text file that lists the output cells within the calculating area. |
| **total_sed_cal.m** | A MATLAB program used to calculate the response statistics from Delft3D output. |


## Execution

Run this experiment with:

```bash
$ dakota -i dakota.in -o dakota.out &> run.log
```

or with the **dakota_utils** package script `dakota_run`:

```bash
$ dakota_run .
```

