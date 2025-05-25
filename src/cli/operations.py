from typing import Callable, NamedTuple
from src.calculator.basic import add, subtract
from src.calculator.scientific import power, log

class Operation(NamedTuple):
    name: str
    func: Callable

operations = [
    Operation(name="Add", func=add),
    Operation(name="Subtract", func=subtract),
    Operation(name="Power", func=power),
    Operation(name="Log", func=log),
]
