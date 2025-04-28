from typing import List


def calculate_returns(prices: List[float]) -> List[float]:
    """
    Calculate the returns for a given price series.
    
    Args:
        prices: List of prices
        
    Returns:
        List of returns
        
    Raises:
        ValueError: If prices list is empty or has only one value
    """
    if len(prices) < 2:
        raise ValueError("Price series must contain at least 2 values")
        
    returns = []
    for i in range(1, len(prices)):
        returns.append((prices[i] - prices[i-1]) / prices[i-1])
        
    return returns 