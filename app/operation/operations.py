from __future__ import annotations
from typing import Iterable
from functools import reduce
import operator

class OperationError(Exception):
    """Custom exception for operation-related errors."""

def _ensure_numbers(values: Iterable[float]) -> list[float]:
    try:
        nums = [float(v) for v in values]
    except (TypeError, ValueError) as exc:
        raise OperationError("All operands must be numeric.") from exc
    if len(nums) == 0:
        raise OperationError("At least one operand is required.")
    return nums

def add(values: Iterable[float]) -> float:
    nums = _ensure_numbers(values
    )
    return float(sum(nums))

def sub(values: Iterable[float]) -> float:
    nums = _ensure_numbers(values)
    first, *rest = nums
    return float(first - sum(rest))

def mul(values: Iterable[float]) -> float:
    nums = _ensure_numbers(values)
    return float(reduce(operator.mul, nums, 1.0))

def div(values: Iterable[float]) -> float:
    nums = _ensure_numbers(values)
    if len(nums) < 2:
        raise OperationError("Division requires at least two operands.")
    result = float(nums[0])
    for d in nums[1:]:
        # EAFP: allow ZeroDivisionError to be raised
        result = result / float(d)
    return float(result)
