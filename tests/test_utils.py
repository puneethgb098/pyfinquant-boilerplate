import pytest
from pyfinquant.utils import calculate_returns


def test_calculate_returns():
    # Test with simple price series
    prices = [100, 105, 110, 115]
    expected_returns = [0.05, 0.0476, 0.0455]
    
    returns = calculate_returns(prices)
    assert len(returns) == len(expected_returns)
    assert all(abs(r - e) < 1e-4 for r, e in zip(returns, expected_returns))
    
    # Test with empty list
    with pytest.raises(ValueError):
        calculate_returns([])
        
    # Test with single value
    with pytest.raises(ValueError):
        calculate_returns([100]) 