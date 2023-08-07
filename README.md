# PathSpotter

PathSpotter provides metrics and code visualization to better support understanding tested paths, including the most and least tested paths as well as their executed lines of code, inputs, outputs, and thrown exceptions.

## Install

First, clone and install SpotFlow:
```
git clone https://github.com/andrehora/spotflow
pip install -e ./spotflow
```

Next, clone PathSpotter:
```
git clone https://github.com/andrehora/pathspotter
pip install -e pathspotter
```

## Quick example

### Generating CSV and HTML reports for the test suite of the Python Standard Library

First, let's generate the reports got the test suite of the `gzip` library:

```
$ python -m spotflow -t gzip -s pathspotter.runner -arg gzip test.test_gzip
```