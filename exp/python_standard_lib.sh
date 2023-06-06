PATHSPOTTER='../pathspotter/runner.py'

python3 -m spotflow -t gzip -s $PATHSPOTTER -arg gzip test.test_gzip
python3 -m spotflow -t email -s pathspotter.py -arg email test.test_email
python3 -m spotflow -t calendar -s pathspotter.py -arg calendar test.test_calendar
python3 -m spotflow -t ftplib -s pathspotter.py -arg ftplib test.test_ftplib
python3 -m spotflow -t collections -s pathspotter.py -arg collections test.test_collections
python3 -m spotflow -t os -s pathspotter.py -arg os test.test_os
python3 -m spotflow -t tarfile -s pathspotter.py -arg tarfile test.test_tarfile
python3 -m spotflow -t pathlib -s pathspotter.py -arg pathlib test.test_pathlib
python3 -m spotflow -t logging -s pathspotter.py -arg logging test.test_logging
python3 -m spotflow -t difflib -s pathspotter.py -arg difflib test.test_difflib
python3 -m spotflow -t imaplib -s pathspotter.py -arg imaplib test.test_imaplib
python3 -m spotflow -t smtplib -s pathspotter.py -arg smtplib test.test_smtplib
python3 -m spotflow -t csv -s pathspotter.py -arg csv test.test_csv
python3 -m spotflow -t argparse -s pathspotter.py -arg argparse test.test_argparse
python3 -m spotflow -t configparser -s pathspotter.py -arg configparser test.test_configparser