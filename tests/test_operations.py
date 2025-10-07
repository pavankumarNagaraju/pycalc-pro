import pytest
from app.operation.operations import add, sub, mul, div, OperationError

@pytest.mark.parametrize("vals, expected", [
    ([1, 2, 3], 6.0),
    ([5.5, 4.5], 10.0),
    ((-1, 1, -2, 2), 0.0),
])
def test_add(vals, expected):
    assert add(vals) == pytest.approx(expected)

@pytest.mark.parametrize("vals, expected", [
    ([10, 2, 3], 5.0),
    ([5.5, 4.5], 1.0),
    ((0, 3), -3.0),
])
def test_sub(vals, expected):
    assert sub(vals) == pytest.approx(expected)

@pytest.mark.parametrize("vals, expected", [
    ([2, 3, 4], 24.0),
    ([1.5, 2], 3.0),
    ((-2, -3), 6.0),
])
def test_mul(vals, expected):
    assert mul(vals) == pytest.approx(expected)

@pytest.mark.parametrize("vals, expected", [
    ([10, 2], 5.0),
    ([100, 5, 2], 10.0),
    ((9, 3, 3), 1.0),
])
def test_div(vals, expected):
    assert div(vals) == pytest.approx(expected)

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div([10, 0])

def test_non_numeric_raises():
    with pytest.raises(OperationError):
        add(["a", 1])
    with pytest.raises(OperationError):
        mul([1, None])

def test_div_needs_two():
    import app.operation.operations as ops
    with pytest.raises(OperationError):
        ops.div([3])
def test_empty_operands_raise_operation_error():
    import pytest
    from app.operation.operations import add, OperationError
    with pytest.raises(OperationError):
        add([])
import pytest
from app.operation.operations import _ensure_numbers, OperationError

def test__ensure_numbers_empty_raises():
    with pytest.raises(OperationError):
        _ensure_numbers([])
