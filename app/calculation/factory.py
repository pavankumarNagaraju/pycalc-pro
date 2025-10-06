from __future__ import annotations
from typing import List
from app.calculation.calculation import Calculation
from app.operation.operations import add, sub, mul, div, OperationError

OP_MAP = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
}

class CalculationFactory:
    @staticmethod
    def create(operation: str, operands: List[float]) -> Calculation:
        op = operation.lower().strip()
        if op not in OP_MAP:
            raise OperationError(f"Unsupported operation: {operation}")
        if len(operands) < 2:
            raise OperationError("Provide at least two numbers.")
        return Calculation(operands=operands, operator=OP_MAP[op])
