import pytest
from app.calculation.factory import CalculationFactory
from app.operation.operations import OperationError

def test_factory_add():
    calc = CalculationFactory.create("add", [1, 2, 3])
    assert calc.compute() == 6.0

@pytest.mark.parametrize("op", ["ADD", " Sub ", "Mul", "div"])
def test_factory_variants(op):
    calc = CalculationFactory.create(op, [2, 2])
    assert isinstance(calc.compute(), float)

def test_factory_requires_two_operands_for_ops():
    with pytest.raises(OperationError):
        CalculationFactory.create("add", [1])

def test_factory_rejects_unknown():
    with pytest.raises(OperationError):
        CalculationFactory.create("pow", [2, 3])
