# invalid_conf_example

In this example the `.ipython/profile_default/ipython_config.py´ file is missing. This causes the magic command to be missing, but it is still present in the help text:

```bash
(venv) danielfalk@Daniels-MacBook-Pro kedro-video-example % kedro ipython
-------------------------------------------------------------------------------
Starting a Kedro session with the following variables in scope
startup_error, context
Use the line magic %reload_kedro to refresh them
or to see the error message if they are undefined
-------------------------------------------------------------------------------
ipython
Python 3.10.1 (main, Jan 16 2022, 18:54:33) [Clang 13.0.0 (clang-1300.0.29.30)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.32.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: %reload_kedro
UsageError: Line magic function `%reload_kedro` not found.

In [2]:
```
