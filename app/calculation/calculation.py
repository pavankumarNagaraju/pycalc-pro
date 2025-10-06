from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Iterable, List

Number = float

@dataclass(frozen=True)
class Calculation:
    operands: List[Number]
    operator: Callable[[Iterable[Number]], Number]

    def compute(self) -> Number:
        return self.operator(self.operands)
