#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Pr2.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def printit():
    threading.Timer(100.0, printit).start()
    if not os.listdir('Pr2/files/media/csv'):
        print('COOL!')
    else:
        print('FUCK!')
printit()
if __name__ == '__main__':
    main()