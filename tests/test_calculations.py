import pytest
from app.calculation.calculation import Calculation
from app.operation.operations import add, sub, mul, div

@pytest.mark.parametrize("operands, op, expected", [
    ([1, 2, 3], add, 6.0),
    ([10, 5], sub, 5.0),
    ([2, 3, 4], mul, 24.0),
    ([9, 3, 3], div, 1.0),
])
def test_calculation_compute(operands, op, expected):
    calc = Calculation(operands=operands, operator=op)
    assert calc.compute() == pytest.approx(expected)
