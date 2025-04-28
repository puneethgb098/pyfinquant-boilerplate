@echo off
REM Windows make.bat for PyFinQuant

REM Development
python -m pip install -e ".[dev]"

REM Testing
python -m pytest tests/

REM Linting
python -m ruff check .
python -m ruff format --check .

REM Type checking
python -m mypy .

REM Documentation
python -m sphinx.cmd.build -b html docs/ docs/_build/html

REM Clean
python -m pip uninstall -y pyfinquant
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q pyfinquant.egg-info
rmdir /s /q docs/_build

REM Help
echo.
echo Available commands:
echo   make install    - Install package in development mode
echo   make test      - Run tests
echo   make lint      - Run linting
echo   make type      - Run type checking
echo   make docs      - Build documentation
echo   make clean     - Clean build files
echo. 