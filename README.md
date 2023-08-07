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

### Exporting the tested paths

First, let's export the tested paths of test suite `test_gzip` of Python Standard Library:

```
$ python -m spotflow -t gzip -s pathspotter.runner -arg gzip test.test_gzip
```

This should produce the following output:

```
Running and monitoring: test.test_gzip
............s................................................
----------------------------------------------------------------------
Ran 61 tests in 2.392s

OK
Report size: 32
1. gzip.open
2. gzip.GzipFile.__init__
3. gzip.GzipFile._init_write
4. gzip.GzipFile._write_gzip_header
5. gzip.write32u
6. gzip.GzipFile.write
7. gzip.GzipFile.close
8. gzip._GzipReader.__init__
9. gzip._PaddedFile.__init__
10. gzip.GzipFile.flush
11. gzip.GzipFile.fileno
12. gzip.GzipFile.read
13. gzip._GzipReader.read
14. gzip._GzipReader._init_read
15. gzip._GzipReader._read_gzip_header
16. gzip._PaddedFile.read
17. gzip._GzipReader._read_exact
18. gzip._PaddedFile.prepend
19. gzip._GzipReader._add_read_data
20. gzip._GzipReader._read_eof
21. gzip.GzipFile.readline
22. gzip.GzipFile.readable
23. gzip.GzipFile.seek
24. gzip._PaddedFile.seekable
25. gzip.compress
26. gzip.decompress
27. gzip.GzipFile.peek
28. gzip.GzipFile.read1
29. gzip._GzipReader._rewind
30. gzip._PaddedFile.seek
31. gzip.GzipFile.writable
32. gzip.GzipFile.seekable
```