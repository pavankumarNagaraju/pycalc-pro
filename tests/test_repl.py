from app.repl import run_repl, HELP_TEXT
from app.calculator.history import History

def run_scripted(inputs):
    it = iter(inputs)
    outputs = []
    def fake_input(prompt=""):
        outputs.append(prompt)
        return next(it)
    def fake_print(msg=""):
        outputs.append(str(msg))
    hist = History()
    run_repl(input_fn=fake_input, output_fn=fake_print, history=hist)
    return outputs, hist

def test_help_and_exit_flow():
    outputs, _ = run_scripted(["help", "exit"])
    assert any("Welcome to the Python Calculator" in line for line in outputs)
    assert HELP_TEXT.strip() in "\n".join(outputs)
    assert any("Goodbye!" in line for line in outputs)

def test_add_then_history_then_exit():
    outputs, hist = run_scripted([
        "add",
        "1, 2, 3",
        "history",
        "exit",
    ])
    assert any("Result: 6.0" in o for o in outputs)
    assert any("add [1.0, 2.0, 3.0] = 6.0" in o for o in outputs)
    assert len(hist.items) == 1

def test_invalid_command_and_input_errors():
    outputs, _ = run_scripted([
        "unknown",
        "add",
        "a, b",
        "div",
        "1, 0",
        "exit",
    ])
    joined = "\n".join(outputs)
    assert "Unknown command" in joined
    assert "Input error: Invalid number" in joined
    assert "Division by zero" in joined
