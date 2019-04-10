#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler

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


if __name__ == '__main__':
    main()
    observer = Observer()
    observer.schedule(print('cool!'), path = 'C:/Users/Артемий/PycharmProjects/Pr2/Pr2/files/media/csv', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
