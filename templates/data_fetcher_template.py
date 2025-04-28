"""
Template for data fetchers in PyFinQuant
"""

from abc import ABC, abstractmethod
from typing import Union, List, Dict
import pandas as pd
import numpy as np

class DataFetcherTemplate(ABC):
    """
    Base template for all data fetchers.
    Inherit from this class to create custom data fetchers.
    """
    
    def __init__(self, **kwargs):
        """
        Initialize data fetcher with parameters
        
        Parameters:
        -----------
        **kwargs : dict
            Fetcher-specific parameters
        """
        self.parameters = kwargs
        self.cache = {}
    
    @abstractmethod
    def fetch_data(
        self,
        tickers: Union[str, List[str]],
        start_date: str = None,
        end_date: str = None,
        period: str = None,
        interval: str = '1d'
    ) -> pd.DataFrame:
        """
        Fetch market data for given tickers
        
        Parameters:
        -----------
        tickers : Union[str, List[str]]
            Ticker symbol(s) to fetch data for
        start_date : str, optional
            Start date in YYYY-MM-DD format
        end_date : str, optional
            End date in YYYY-MM-DD format
        period : str, optional
            Time period (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')
        interval : str, optional
            Data interval (e.g., '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo')
            
        Returns:
        --------
        pd.DataFrame
            Market data
        """
        pass
    
    def preprocess_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess market data
        
        Parameters:
        -----------
        data : pd.DataFrame
            Raw market data
            
        Returns:
        --------
        pd.DataFrame
            Preprocessed data
        """
        # Template implementation - override in child class
        processed = data.copy()
        
        # Handle missing values
        processed = processed.fillna(method='ffill').fillna(method='bfill')
        
        # Calculate additional columns
        processed['Returns'] = processed['Close'].pct_change()
        processed['Log_Returns'] = np.log(processed['Close']).diff()
        
        return processed
    
    def cache_data(self, key: str, data: pd.DataFrame) -> None:
        """
        Cache fetched data
        
        Parameters:
        -----------
        key : str
            Cache key
        data : pd.DataFrame
            Data to cache
        """
        self.cache[key] = data
    
    def get_cached_data(self, key: str) -> pd.DataFrame:
        """
        Get cached data
        
        Parameters:
        -----------
        key : str
            Cache key
            
        Returns:
        --------
        pd.DataFrame
            Cached data
        """
        return self.cache.get(key) 