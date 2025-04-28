"""
Template for backtesting engines in PyFinQuant
"""

from typing import Dict, Any
import pandas as pd
import numpy as np

class BacktestTemplate:
    """
    Template for creating backtesting engines.
    Inherit from this class to create custom backtesting engines.
    """
    
    def __init__(self, **kwargs):
        """
        Initialize backtest engine with parameters
        
        Parameters:
        -----------
        **kwargs : dict
            Backtest-specific parameters
        """
        self.parameters = kwargs
        self.results = {}
    
    def run(self, data: pd.DataFrame, strategy: Any) -> Dict[str, Any]:
        """
        Run backtest with given data and strategy
        
        Parameters:
        -----------
        data : pd.DataFrame
            Market data
        strategy : Any
            Trading strategy object
            
        Returns:
        --------
        Dict[str, Any]
            Backtest results
        """
        # Generate signals
        signals = strategy.generate_signals(data)
        
        # Calculate positions
        positions = strategy.calculate_position_size(
            signals, 
            self.parameters.get('initial_capital', 100000)
        )
        
        # Calculate returns
        returns = strategy.calculate_returns(data, positions)
        
        # Calculate metrics
        metrics = strategy.calculate_metrics(returns)
        
        # Store results
        self.results = {
            'signals': signals,
            'positions': positions,
            'returns': returns,
            'metrics': metrics
        }
        
        return self.results
    
    def plot_results(self) -> None:
        """
        Plot backtest results
        """
        # Template implementation - override in child class
        pass
    
    def generate_report(self) -> str:
        """
        Generate backtest report
        
        Returns:
        --------
        str
            Report text
        """
        # Template implementation - override in child class
        report = f"""
        Backtest Report
        --------------
        Total Return: {self.results['metrics']['total_return']:.2%}
        Annual Return: {self.results['metrics']['annual_return']:.2%}
        Sharpe Ratio: {self.results['metrics']['sharpe_ratio']:.2f}
        Max Drawdown: {self.results['metrics']['max_drawdown']:.2%}
        """
        return report 