## Prerequisites
To run this package `python3.10` is reccomended. On early stages of developing this project this might not be important, but all further dependencies can require 3.10 version only.

## How to install?
Installing this is simple, just write to the terminal:
```
pip install robustprinter
```

# About

## History
This package was born in desparate search for the tool to conveniently print training information to the console. Altough Tensorflow has its own pre-built printer, which is quite nice, pytorch doesn't have such luxuary. Most of my applications depend on torch and I was tired of tedious print statements around my code that was hard to make beautiful.

Main idea is to incapsulate functionality that I may use across different other applications in one package.

## Usage
Main classes are `Printer` and `Formatter`. Printer regulates what, when and where something must be printed and Formatter regulates how it must be printed. For now package has only `DefaultFormatter` class – child of `Formatter`, and all it does is prints beautifully training info.

To see package in work try this code:
```py
import time
import numpy as np
from robustprinter import Printer, formatter
from robustprinter.formatter import DefaultFormatter

class TestFormatter(formatter.Formatter):
    def __init__(self) -> None:
        super(TestFormatter, self).__init__()
    
    def format(self, data) -> str:
        return data
    
metrics_list = [
    'precision', 'recall', 'mAP50', 'mAP50-95', 'accuracy',
    'FID', 'loss'
]

def generate_random_metrics(metrics: list) -> dict:
    result = dict()
    for metric in metrics:
        result[metric] = np.random.rand()
    return result

if __name__ == '__main__':
    print('Start test.')
    max_steps = 10

    rformatter = DefaultFormatter(max_steps=max_steps, max_columns=2)
    rprinter = Printer(formatter=rformatter)
    rprinter.start()

    data = dict()
    for epoch in range(3):
        data['epoch'] = epoch
        for step in range(max_steps):
            data['step'] = step + 1
            data['partition'] = 'train'
            data['metrics'] = generate_random_metrics(metrics=metrics_list)

            rprinter.print(data=data)
            time.sleep(1)
        rprinter.break_loop()
```

# Examples

## DefaultFormatter
![DefaultFormatter](./misc/Example:%20DefaultFormatter.png)

# Contribution
This repository is about designing new formatters and printers. If you have an idea and want to share it – you are welcome!