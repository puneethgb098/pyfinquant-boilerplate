# PyFinQuant Boilerplate

[![Python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![UV](https://img.shields.io/badge/UV-0.1.0-FFD43B?logo=python&logoColor=black)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/badge/Ruff-0.1.0-FF4B4B?logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff)
[![Sphinx](https://img.shields.io/badge/Sphinx-4.0.0-1A1A1A?logo=sphinx&logoColor=white)](https://www.sphinx-doc.org/)
[![Mypy](https://img.shields.io/badge/Mypy-0.910-1A1A1A?logo=python&logoColor=white)](https://mypy-lang.org/)
[![Codecov](https://img.shields.io/badge/Codecov-F01F7A?logo=codecov&logoColor=white)](https://codecov.io/)

A modern Python boilerplate for quantitative finance projects, providing a robust foundation for building financial analysis, backtesting, and portfolio optimization tools.

## 🚀 Features

- **Modern Development Setup**:
  - UV for fast dependency management
  - Ruff for lightning-fast linting and formatting
  - Pre-commit hooks for code quality
  - Type checking with mypy
  - Comprehensive testing setup

- **Project Structure**:
  - Clean, modular architecture
  - Sphinx documentation setup
  - GitHub Actions CI/CD pipeline
  - Cross-platform development support

- **Development Tools**:
  - Makefile for common tasks
  - Windows support with make.bat
  - Pre-configured development environment
  - Automated code quality checks

## 📦 Installation

For development installation:

```powershell
# Clone the repository
git clone https://github.com/yourusername/pyfinquant-boilerplate.git
cd pyfinquant-boilerplate

# Install with UV (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
uv pip install -e ".[dev]"

# Or install with pip
pip install -e ".[dev]"
```

## 🛠️ Development

```powershell
# Run tests
.\make.bat test

# Run linting
.\make.bat lint

# Build documentation
.\make.bat docs

# Clean build files
.\make.bat clean
```

## 📚 Documentation

The documentation is built using Sphinx and includes:

- Installation guide
- Usage examples
- API reference
- Contribution guidelines
- Changelog

Build the documentation locally:

```powershell
.\make.bat docs
```

## 🤝 Contributing

This is a boilerplate project designed to be customized. To use it:

1. Fork this repository
2. Customize the project structure and templates
3. Update the documentation
4. Add your specific implementation

For contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Puneeth G B - puneethgb30@gmail.com

[LinkedIn](https://www.linkedin.com/in/puneeth-g-b-463aa91a0/)
