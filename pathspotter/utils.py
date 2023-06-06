import os
import re
import shutil
import csv
from collections import Counter
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name


def full_filename(local_dir, filename, file_origin):
    dir_path = os.path.dirname(file_origin)
    return os.path.join(dir_path, local_dir, filename)


def full_dir(local_dir, file_origin):
    dir_path = os.path.dirname(file_origin)
    return os.path.join(dir_path, local_dir)


def ensure_dir(directory):
    if directory:
        os.makedirs(directory, exist_ok=True)


def copy_files(local_dir, files, destination, file_origin=__file__):
    for file in files:
        from_file = full_filename(local_dir, file, file_origin)
        to_file = full_filename(destination, file, file_origin)
        shutil.copyfile(from_file, to_file)


def read_file(filename):
    with open(filename) as f:
        return f.read()
    

def write_html(filename, content):
    html = re.sub(r"(\A\s+)|(\s+$)", "", content, flags=re.MULTILINE) + "\n"
    with open(filename, "wb") as fout:
        fout.write(html.encode("ascii", "xmlcharrefreplace"))


def write_csv(filename, content):
    with open(filename, "w") as fout:
        wr = csv.writer(fout, quoting=csv.QUOTE_ALL)
        wr.writerows(content)