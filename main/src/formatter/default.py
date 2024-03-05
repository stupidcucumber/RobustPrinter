from .base import Formatter
from typing import Any


class DefaultFormatter(Formatter):
    def __init__(self, max_steps: int, max_columns: int, precision: int=3) -> None:
        super(DefaultFormatter, self).__init__()
        self.max_columns = max_columns
        self.max_steps = max_steps
        self.precision = precision

    def _make_text_bold(self, text: str) -> str:
        return '\033[41m' + text + '\033[0m'

    def _construct_loading(self, current_step: int) -> str:
        fill_symbol = '='
        percentage = int(100 * current_step / self.max_steps) 
        return '[%s]' % ((fill_symbol * percentage) + ('-' * (100 - percentage)), )

    def format(self, data: Any) -> str:
        partition = data['partition']
        epoch = data['epoch']
        step = data['step']
        metrics = data['metrics']

        result = 'Result of %s on epoch %s. Step %d/%d: %s' \
            % (partition, epoch, step, self.max_steps, self._construct_loading(current_step=step))
        for index, (metric_name, metric_value) in enumerate(metrics.items()):
            if index % self.max_columns == 0:
                result += '\n'
            bmetric_name = self._make_text_bold(metric_name)
            result += '%s:  %s  ' % (bmetric_name, ('%' + '0.%df' % self.precision) % metric_value)

        return result
