from typing import Callable, NamedTuple
from src.calculator.basic import add, subtract

class Operation(NamedTuple):
    name: str
    func: Callable

operations = [
    Operation(name="Add", func=add),
    Operation(name="Subtract", func=subtract),
]
