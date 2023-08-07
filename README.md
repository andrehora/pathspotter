[![pages-build-deployment](https://github.com/andrehora/pathspotter/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/andrehora/pathspotter/actions/workflows/pages/pages-build-deployment)

# PathSpotter

PathSpotter provides metrics and code visualization to support understanding the *tested paths* of a Python method.
A *tested path* of a method represents a set of input values that will make the method behave in the same way, that is, execute the same lines of code.

PathSpotter generates CSV and [HTML reports like this](https://andrehora.github.io/pathspotter/report_html/calendar).

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

## Quick example

Let's export the tested paths of the test suite `test_gzip` of the Python Standard Library.
This command should generate reports in HTML and CSV formats:

```
python3 -m spotflow -t gzip -s pathspotter/pathspotter/runner.py -arg gzip test.test_gzip
```

Then, open the folders `report_html/gzip` and `report_csv/gzip` to see reports like these: [HTML](https://andrehora.github.io/pathspotter/report_html/gzip) and [CSV](https://github.com/andrehora/pathspotter/tree/main/report_csv/gzip).

See more examples [here](https://github.com/andrehora/pathspotter/blob/main/examples/python_libs.sh).


## Explore other tested paths

### Python Standard Library

- [argparse](https://andrehora.github.io/pathspotter/report_html/argparse)
- [email](https://andrehora.github.io/pathspotter/report_html/email)
- [tarfile](https://andrehora.github.io/pathspotter/report_html/tarfile)
- [pathlib](https://andrehora.github.io/pathspotter/report_html/pathlib)
- [configparser](https://andrehora.github.io/pathspotter/report_html/configparser)
- [os](https://andrehora.github.io/pathspotter/report_html/os)
- [logging](https://andrehora.github.io/pathspotter/report_html/logging)
- [csv](https://andrehora.github.io/pathspotter/report_html/csv)
- [collections](https://andrehora.github.io/pathspotter/report_html/collections)
- [imaplib](https://andrehora.github.io/pathspotter/report_html/imaplib)
- [ftplib](https://andrehora.github.io/pathspotter/report_html/ftplib)
- [smtplib](https://andrehora.github.io/pathspotter/report_html/smtplib)
- [calendar](https://andrehora.github.io/pathspotter/report_html/calendar)
- [gzip](https://andrehora.github.io/pathspotter/report_html/gzip)
- [difflib](https://andrehora.github.io/pathspotter/report_html/difflib)

### Other software systems

- [DateUtil](https://andrehora.github.io/pathspotter/report_html/dateutil)
- [TheFuck](https://andrehora.github.io/pathspotter/report_html/thefuck)
- [Pylint](https://andrehora.github.io/pathspotter/report_html/pylint)
- [Rich](https://andrehora.github.io/pathspotter/report_html/rich)
- [Requests](https://andrehora.github.io/pathspotter/report_html/requests)
- [Flask](https://andrehora.github.io/pathspotter/report_html/flask)
- [Cookiecutter](https://andrehora.github.io/pathspotter/report_html/cookiecutter)
- [Six](https://andrehora.github.io/pathspotter/report_html/six)
- [BentoML](https://andrehora.github.io/pathspotter/report_html/bentoml)
- [Jupyter Client](https://andrehora.github.io/pathspotter/report_html/jupyter_client)