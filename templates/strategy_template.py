"""
Template for creating trading strategies in PyFinQuant
"""

from abc import ABC, abstractmethod
import pandas as pd
import numpy as np

class StrategyTemplate(ABC):
    """
    Base template for all trading strategies.
    Inherit from this class to create custom strategies.
    """
    
    def __init__(self, **kwargs):
        """
        Initialize strategy with parameters
        
        Parameters:
        -----------
        **kwargs : dict
            Strategy-specific parameters
        """
        self.parameters = kwargs
    
    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Generate trading signals from market data
        
        Parameters:
        -----------
        data : pd.DataFrame
            Market data with OHLCV columns
            
        Returns:
        --------
        pd.DataFrame
            DataFrame containing trading signals
        """
        pass
    
    def calculate_position_size(self, signals: pd.DataFrame, capital: float) -> pd.DataFrame:
        """
        Calculate position sizes based on signals and capital
        
        Parameters:
        -----------
        signals : pd.DataFrame
            Trading signals
        capital : float
            Available capital
            
        Returns:
        --------
        pd.DataFrame
            Position sizes
        """
        # Template implementation - override in child class
        positions = signals.copy()
        positions['position'] = positions['signal'] * capital
        return positions
    
    def calculate_returns(self, data: pd.DataFrame, positions: pd.DataFrame) -> pd.Series:
        """
        Calculate strategy returns
        
        Parameters:
        -----------
        data : pd.DataFrame
            Market data
        positions : pd.DataFrame
            Position sizes
            
        Returns:
        --------
        pd.Series
            Strategy returns
        """
        # Template implementation - override in child class
        returns = data['Close'].pct_change()
        strategy_returns = returns * positions['position'].shift(1)
        return strategy_returns
    
    def calculate_metrics(self, returns: pd.Series) -> dict:
        """
        Calculate strategy performance metrics
        
        Parameters:
        -----------
        returns : pd.Series
            Strategy returns
            
        Returns:
        --------
        dict
            Performance metrics
        """
        # Template implementation - override in child class
        metrics = {
            'total_return': (1 + returns).prod() - 1,
            'annual_return': (1 + returns).prod() ** (252/len(returns)) - 1,
            'sharpe_ratio': np.sqrt(252) * returns.mean() / returns.std(),
            'max_drawdown': (returns.cumsum().expanding().max() - returns.cumsum()).max()
        }
        return metrics 