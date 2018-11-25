#!C:\Users\vijay.kiran\Desktop\Lilly_app_automation\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pycmd==1.2','console_scripts','py.countloc'
__requires__ = 'pycmd==1.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pycmd==1.2', 'console_scripts', 'py.countloc')()
    )
