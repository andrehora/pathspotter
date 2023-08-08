[![pages-build-deployment](https://github.com/andrehora/pathspotter/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/andrehora/pathspotter/actions/workflows/pages/pages-build-deployment)

# PathSpotter

PathSpotter provides metrics and code visualization to support understanding the *tested paths* of a Python method.
A *tested path* of a method represents a set of input values that will make the method behave in the same way, that is, execute the same lines of code.

PathSpotter generates [HTML reports like this](https://andrehora.github.io/pathspotter/examples/report_html/calendar).

## Install

First, create a virtual environment (and activate it):

```
python3 -m venv .venv			
source .venv/bin/activate
```

Next, clone and install [SpotFlow](https://github.com/andrehora/spotflow):
```
git clone https://github.com/andrehora/spotflow
pip install -e ./spotflow
```

Then, clone and install PathSpotter:
```
git clone https://github.com/andrehora/pathspotter
pip install -e ./pathspotter
```

## Quick usage

Let's export the tested paths of the test suite `test_gzip` of the Python Standard Library.
This command should generate reports in HTML and CSV formats:

```
python3 -m spotflow -t gzip -s pathspotter/pathspotter/runner.py -arg gzip test.test_gzip
```

Then, open the file `report_html/gzip/index.html` to see reports [like this](https://andrehora.github.io/pathspotter/examples/report_html/gzip).



## Detailed usage