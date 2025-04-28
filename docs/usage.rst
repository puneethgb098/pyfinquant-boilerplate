Usage
=====

This section provides examples of how to use PyFinQuant.

Basic Usage
----------

Fetching Data
~~~~~~~~~~~~

.. code-block:: python

    from pyfinquant.data_fetcher import DataFetcher
    
    fetcher = DataFetcher()
    data = fetcher.get_data(
        symbols=['AAPL', 'MSFT'],
        start_date='2020-01-01',
        end_date='2023-12-31'
    )

Creating a Strategy
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from pyfinquant.strategy import BaseStrategy
    
    class SimpleStrategy(BaseStrategy):
        def generate_signals(self):
            # Implement your strategy logic here
            pass

Running a Backtest
~~~~~~~~~~~~~~~~

.. code-block:: python

    from pyfinquant.backtest import Backtest
    
    strategy = SimpleStrategy()
    backtest = Backtest(
        strategy=strategy,
        data=data,
        initial_capital=100000
    )
    results = backtest.run()

Advanced Usage
------------

Portfolio Optimization
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from pyfinquant.portfolio import Portfolio
    
    portfolio = Portfolio(
        returns=returns,
        risk_free_rate=0.02
    )
    weights = portfolio.optimize()

Risk Management
~~~~~~~~~~~~~

.. code-block:: python

    from pyfinquant.risk import RiskManager
    
    risk_manager = RiskManager(
        returns=returns,
        positions=positions
    )
    risk_metrics = risk_manager.calculate_metrics()

Performance Analysis
~~~~~~~~~~~~~~~~~

.. code-block:: python

    from pyfinquant.performance import PerformanceAnalyzer
    
    analyzer = PerformanceAnalyzer(returns=returns)
    metrics = analyzer.calculate_metrics()
    
    # Plot results
    analyzer.plot_performance() 