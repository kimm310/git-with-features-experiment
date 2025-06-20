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

def get_operation_from_user() -> Operation:
    print("Available operations:")
    for idx, operation in enumerate(operations, 1):
        print(f"{idx}. {operation.name}")

    while True:
        try:
            operation_id = int(input("Enter the operation number: ")) - 1
            if 0 <= operation_id < len(operations):
                result = operations[operation_id]
                print(f"Selected operation: {result.name}")
                return result
            else:
                print("Invalid ID. Please select a valid operation.")
        except ValueError:
            print("Please enter a valid number.")
