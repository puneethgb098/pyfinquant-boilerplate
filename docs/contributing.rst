Contributing
============

We welcome contributions to PyFinQuant! Here's how you can help:

Getting Started
--------------

1. Fork the repository
2. Clone your fork
3. Create a new branch for your feature
4. Install development dependencies:

.. code-block:: bash

    pip install -e ".[dev]"

Development Workflow
------------------

1. Write your code following the project's style guide
2. Add tests for your code
3. Run the test suite:

.. code-block:: bash

    make test

4. Ensure all linting checks pass:

.. code-block:: bash

    make lint

5. Submit a pull request

Code Style
---------

- Follow PEP 8 guidelines
- Use type hints
- Document all public functions and classes
- Write docstrings in Google style

Testing
-------

- Write unit tests for all new code
- Ensure test coverage remains high
- Run tests before submitting PRs

Documentation
------------

- Update documentation for new features
- Add examples where appropriate
- Keep the changelog up to date

Pull Request Process
------------------

1. Update the README.md with details of changes
2. Update the CHANGELOG.md
3. The PR must pass all CI checks
4. At least one maintainer must approve the PR 