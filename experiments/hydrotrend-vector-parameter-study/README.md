# HydroTrend Vector Parameter Study

In this computer experiment,
a vector parameter study of HydroTrend
is performed with Dakota.

## Notes

* The **run_model.py** script is a generic interface to call a
  model. It uses the HydroTrend model defined in `dakota_utils.models`.
* The `analysis_components` keyword in the `methods` section of the
  Dakota input file is used to pass the name of the model to the
  script.
