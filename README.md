# invalid_conf_example

In this example the catalog config contains an invalid specification of the dataset.

If starting the ipython terminal everythink looks fine excepot that the kedro specific variables are not specified in the help text. Trying to use the will result in a warning that they are not defined:
```python
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
2022-02-25 20:28:47,719 - kedro.framework.session.store - INFO - `read()` not implemented for `BaseSessionStore`. Assuming empty store.
2022-02-25 20:28:47,760 - root - WARNING - Kedro extension was registered. Make sure you pass the project path to `%reload_kedro` or set it using `%init_kedro`.

In [1]: catalog.list()
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-486c331608ac> in <cell line: 1>()
----> 1 catalog.list()

NameError: name 'catalog' is not defined
```

calling the magic command `%reload_kedro` will however give a usefull stacktrace:
```python
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
2022-02-25 20:28:47,719 - kedro.framework.session.store - INFO - `read()` not implemented for `BaseSessionStore`. Assuming empty store.
2022-02-25 20:28:47,760 - root - WARNING - Kedro extension was registered. Make sure you pass the project path to `%reload_kedro` or set it using `%init_kedro`.

In [1]: %reload_kedro
[...]
~/src/kedro/kedro/io/data_catalog.py in from_config(cls, catalog, credentials, load_versions, save_version, journal)
    321 
    322             ds_config = _resolve_credentials(ds_config, credentials)
--> 323             data_sets[ds_name] = AbstractDataSet.from_config(
    324                 ds_name, ds_config, load_versions.get(ds_name), save_version
    325             )

~/src/kedro/kedro/io/core.py in from_config(cls, name, config, load_version, save_version)
    143             )
    144         except Exception as exc:
--> 145             raise DataSetError(
    146                 f"An exception occurred when parsing config "
    147                 f"for DataSet `{name}`:\n{str(exc)}"

DataSetError: An exception occurred when parsing config for DataSet `test_ds`:
Class `datasets.invalid` not found or one of its dependencies has not been installed.
```
