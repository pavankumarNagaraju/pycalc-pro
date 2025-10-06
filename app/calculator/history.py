from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class HistoryItem:
    operation: str
    operands: list[float]
    result: float

@dataclass
class History:
    items: List[HistoryItem] = field(default_factory=list)

    def add(self, item: HistoryItem) -> None:
        self.items.append(item)

    def clear(self) -> None:
        self.items.clear()
