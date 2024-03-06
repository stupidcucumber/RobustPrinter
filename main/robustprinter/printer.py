import sys
from typing import Any
from .formatter import Formatter


class Printer:
    def __init__(self, formatter: Formatter) -> None:
        self.formatter = formatter
        self.isstarted = False

    def break_loop(self):
        print()
        self._save_cursor()

    def start(self):
        self._save_cursor()
        self.isstarted = True

    def _restore_cursor(self):
        sys.stdout.write('\033[u\033[J')
        sys.stdout.flush()

    def _save_cursor(self):
        sys.stdout.write('\033[s')
        sys.stdout.flush()

    def print(self, data: Any) -> None:
        if not self.isstarted:
            raise RuntimeError('Printer must be started for the proper displaying of info!')
        self._restore_cursor()
        formatted_data = self.formatter.format(data=data)
        print(formatted_data)
