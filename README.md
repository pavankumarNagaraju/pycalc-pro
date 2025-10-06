# pycalc-pro — CLI Calculator

Minimal modular terminal calculator with REPL, tests, and CI.

## Quick start

### Setup
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip pytest pytest-cov
```

### Run
```powershell
python -m app.repl
```

### Test with coverage
```powershell
python -m pytest --cov=app --cov-report=term-missing
```

Features: add, sub, mul, div, history, help, exit.
LBYL input validation and EAFP error handling.
CI example in .github/workflows/python-app.yml.

![CI](https://github.com/pavankumarNagaraju/pycalc-pro/actions/workflows/python-app.yml/badge.svg)
