from app.calculator.history import History, HistoryItem

def test_history_add_and_clear():
    h = History()
    assert h.items == []
    item = HistoryItem(operation="add", operands=[1,2], result=3.0)
    h.add(item)
    assert h.items == [item]
    h.clear()
    assert h.items == []
