export PYTHONPATH='/Users/andrehora/Documents/git/spotflow'

# Python libs
python3 -m spotflow -t gzip -s happypath.py -arg html/gzip test.test_gzip
python3 -m spotflow -t email -s happypath.py -arg html/email test.test_email
python3 -m spotflow -t calendar -s happypath.py -arg html/calendar test.test_calendar
python3 -m spotflow -t ftplib -s happypath.py -arg html/ftplib test.test_ftplib
python3 -m spotflow -t collections -s happypath.py -arg html/collections test.test_collections
python3 -m spotflow -t os -s happypath.py -arg html/os test.test_os
python3 -m spotflow -t tarfile -s happypath.py -arg html/tarfile test.test_tarfile
python3 -m spotflow -t pathlib -s happypath.py -arg html/pathlib test.test_pathlib
python3 -m spotflow -t logging -s happypath.py -arg html/logging test.test_logging
python3 -m spotflow -t difflib -s happypath.py -arg html/difflib test.test_difflib
python3 -m spotflow -t imaplib -s happypath.py -arg html/imaplib test.test_imaplib
python3 -m spotflow -t smtplib -s happypath.py -arg html/smtplib test.test_smtplib
python3 -m spotflow -t csv -s happypath.py -arg html/csv test.test_csv
python3 -m spotflow -t argparse -s happypath.py -arg html/argparse test.test_argparse
python3 -m spotflow -t configparser -s happypath.py -arg html/configparser test.test_configparser