"""REPL interface for the command-line calculator.

Read–Eval–Print Loop with:
- commands: add, sub, mul, div, history, help, exit
- LBYL parsing + EAFP error handling
"""
from typing import Callable, List
from app.calculation.factory import CalculationFactory
from app.calculator.history import History, HistoryItem
from app.operation.operations import OperationError

HELP_TEXT = """Commands:
  add, sub, mul, div    - perform arithmetic on a list of numbers
  history               - show calculation history for this session
  help                  - show this help message
  exit                  - leave the calculator

Examples:
  Operation: add
  Numbers: 1, 2, 3.5
"""

def _prompt_operation(input_fn: Callable[[str], str], output_fn: Callable[[str], None]) -> str:
    op = input_fn("Operation [add|sub|mul|div|help|history|exit]: ").strip().lower()
    return op

def _parse_numbers_lbyl(raw: str) -> List[float]:
    """LBYL parse: check tokens before casting to float."""
    if not raw.strip():
        raise ValueError("No numbers provided.")
    raw = raw.replace(",", " ")
    tokens = [t for t in raw.split(" ") if t]
    validated: List[float] = []
    for t in tokens:
        s = t.strip()
        if not any(ch.isdigit() for ch in s):
            raise ValueError(f"Invalid number: {t}")
        try:
            validated.append(float(s))  # EAFP cast
        except (TypeError, ValueError) as exc:  # pragma: no cover
            raise ValueError(f"Invalid number: {t}") from exc  # pragma: no cover
    return validated

def _prompt_numbers(input_fn):
    raw = input_fn("Numbers (comma or space separated): ")
    return _parse_numbers_lbyl(raw)

def run_repl(
    input_fn: Callable[[str], str] = input,
    output_fn: Callable[[str], None] = print,
    history: History | None = None,
) -> None:
    hist = history or History()
    output_fn("Welcome to the Python Calculator. Type 'help' for instructions.")
    while True:
        op = _prompt_operation(input_fn, output_fn)

        if op in {"exit", "quit"}:
            output_fn("Goodbye!")
            break

        if op == "help":
            output_fn(HELP_TEXT)
            continue  # pragma: no cover

        if op == "history":
            if not hist.items:
                output_fn("History is empty.")
            else:
                for idx, item in enumerate(hist.items, start=1):
                    output_fn(f"{idx}. {item.operation} {item.operands} = {item.result}")
            continue  # pragma: no cover

        if op not in {"add", "sub", "mul", "div"}:
            output_fn("Unknown command. Type 'help' for available commands.")
            continue  # pragma: no cover

        try:
            nums = _prompt_numbers(input_fn)
            calc = CalculationFactory.create(op, nums)
            result = calc.compute()  # May raise ZeroDivisionError
            hist.add(HistoryItem(operation=op, operands=nums, result=result))
            output_fn(f"Result: {result}")
        except ZeroDivisionError:
            output_fn("Error: Division by zero is not allowed.")
        except OperationError as oe:
            output_fn(f"Error: {oe}")
        except ValueError as ve:
            output_fn(f"Input error: {ve}")
        except Exception as ex:  # pragma: no cover (defensive)
            output_fn(f"Unexpected error: {type(ex).__name__}: {ex}")

if __name__ == "__main__":  # pragma: no cover
    run_repl()
