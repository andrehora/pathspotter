[![pages-build-deployment](https://github.com/andrehora/pathspotter/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/andrehora/pathspotter/actions/workflows/pages/pages-build-deployment)

# PathSpotter

PathSpotter provides metrics and code visualization to support understanding the *tested paths* of a Python method.
A *tested path* of a method represents a set of input values that will make the method behave in the same way, that is, execute the same lines of code.

PathSpotter generates [HTML reports like this](https://andrehora.github.io/pathspotter/examples/report_html/calendar).

## Install

First, create a virtual environment (and activate it):

```shell
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

Let's export the tested paths for the test suite `test_gzip` of the Python Standard Library.
This command generates reports in HTML and CSV formats:

```shell
python3 -m spotflow -t gzip -s pathspotter/pathspotter/runner.py -arg gzip test.test_gzip
```

Then, open the file `report_html/gzip/index.html` to see an [HTML report like this](https://andrehora.github.io/pathspotter/examples/report_html/gzip).
Open the folder `report_csv/gzip` to see a [CSV report like this](https://github.com/andrehora/pathspotter/blob/main/examples/report_csv/gzip).


## Usage details

This command line runs and monitors a test suite called `<test_suite>` with [SpotFlow](https://github.com/andrehora/spotflow) and generates PathSpotter reports:

```shell
python3 -m spotflow -t <target_sut> -s <pathspotter_script> -arg <report_folder_name> <test_suite>

# Examples
python3 -m spotflow -t gzip -s pathspotter/pathspotter/runner.py -arg gzip test.test_gzip
python3 -m spotflow -t csv -s pathspotter/pathspotter/runner.py -arg csv test.test_csv
python3 -m spotflow -t calendar -s pathspotter/pathspotter/runner.py -arg calendar test.test_calendar
```

The first argument `-t` sets the target SUT to be monitored.
The second argument `-s` sets the PathSpotter script that is executed to generate CSV and HTML reports.
The third argument `-arg` sets the report folder name.
The final argument (`<test_suite>`) is the command to execute the test suite.


## More reports

See the repository [tested_paths_dataset](https://github.com/andrehora/tested_paths_dataset) for more reports of popular projects, like [Rich](xxx), [Flask](xxx), and [Pylint](xxx).