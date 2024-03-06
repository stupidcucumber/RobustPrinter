from typing import Any


class Formatter:
    def format(self, data: Any) -> str:
        raise NotImplementedError('This method must be implemented in the derived class.')