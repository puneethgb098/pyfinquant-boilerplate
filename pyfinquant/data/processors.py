"""
Data processing utilities for financial data.
"""

import numpy as np
import pandas as pd
from typing import Optional, List, Union


class DataProcessor:
    """
    Class for processing financial data.
    """
    
    @staticmethod
    def calculate_returns(data: pd.DataFrame, column: str = 'Close') -> pd.Series:
        """
        Calculate percentage returns.
        
        Parameters:
        -----------
        data : pd.DataFrame
            Price data
        column : str
            Column name to use for returns calculation
            
        Returns:
        --------
        pd.Series
            Percentage returns
        """
        return data[column].pct_change()
    
    @staticmethod
    def calculate_log_returns(data: pd.DataFrame, column: str = 'Close') -> pd.Series:
        """
        Calculate logarithmic returns.
        
        Parameters:
        -----------
        data : pd.DataFrame
            Price data
        column : str
            Column name to use for returns calculation
            
        Returns:
        --------
        pd.Series
            Logarithmic returns
        """
        return np.log(data[column]).diff()
    
    @staticmethod
    def add_moving_average(data: pd.DataFrame, window: int, column: str = 'Close') -> pd.DataFrame:
        """
        Add moving average column to data.
        
        Parameters:
        -----------
        data : pd.DataFrame
            Price data
        window : int
            Window size for moving average
        column : str
            Column name to calculate moving average for
            
        Returns:
        --------
        pd.DataFrame
            Data with moving average column
        """
        result = data.copy()
        result[f'MA_{window}'] = result[column].rolling(window=window).mean()
        return result
    
    @staticmethod
    def add_bollinger_bands(
        data: pd.DataFrame, 
        window: int = 20, 
        num_std: float = 2.0, 
        column: str = 'Close'
    ) -> pd.DataFrame:
        """
        Add Bollinger Bands to data.
        
        Parameters:
        -----------
        data : pd.DataFrame
            Price data
        window : int
            Window size for moving average
        num_std : float
            Number of standard deviations for bands
        column : str
            Column name to calculate Bollinger Bands for
            
        Returns:
        --------
        pd.DataFrame
            Data with Bollinger Bands columns
        """
        result = data.copy()
        
        # Calculate moving average
        result[f'MA_{window}'] = result[column].rolling(window=window).mean()
        
        # Calculate standard deviation
        std = result[column].rolling(window=window).std()
        
        # Calculate upper and lower bands
        result[f'BB_Upper_{window}'] = result[f'MA_{window}'] + (std * num_std)
        result[f'BB_Lower_{window}'] = result[f'MA_{window}'] - (std * num_std)
        
        return result 