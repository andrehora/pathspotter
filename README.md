# PathSpotter

PathSpotter provides metrics and code visualization to better support understanding tested paths, including the most and least tested paths as well as their executed lines of code, inputs, outputs, and thrown exceptions.

## Install

First, clone and install SpotFlow:
```
git clone https://github.com/andrehora/spotflow
pip install -e ./spotflow
```

Next, clone and install PathSpotter:
```
git clone https://github.com/andrehora/pathspotter
pip install -e ./pathspotter
```

## Quick example

### Exporting the tested paths

First, let's export the tested paths of test suite `test_gzip` of the Python Standard Library:

```
$ python -m spotflow -t gzip -s pathspotter/pathspotter/runner.py -arg gzip test.test_gzip
```

This command should export the tested paths in HTML and CSV formats.

The following output should be generated, indicating that the HTML and CSV reports were successfully exported:

```
Running and monitoring: test.test_gzip
............s................................................
----------------------------------------------------------------------
Ran 61 tests in 2.511s

OK (skipped=1)
Report size: 32
1. gzip.open
2. gzip.GzipFile.__init__
3. gzip.GzipFile._init_write
4. gzip.GzipFile._write_gzip_header
5. gzip.write32u
6. gzip.GzipFile.write
...
PathSpotter HTML report: ./report_html/gzip
PathSpotter CSV report: ./report_csv/gzip
```

Then, open the folders `report_html/gzip` and `report_csv/gzip` to see a [HTML report like this](https://andrehora.github.io/pathspotter/report_html/gzip) and [CSV report like this](https://github.com/andrehora/pathspotter/tree/main/docs/report_csv/gzip).