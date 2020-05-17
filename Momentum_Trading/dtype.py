import numpy as np

def generate_positions(prices):
    """
    Generate the following signals:
     - Long 30 share of stock when the price is above 50 dollars
     - Short 10 shares when it's below 20 dollars
    
    Parameters
    ----------
    prices : DataFrame
        Prices for each ticker and date
    
    Returns
    -------
    final_positions : DataFrame
        Final positions for each ticker and date
    """
    long = (prices > 50).astype(int)*30
    short = (prices < 20).astype(int)*-10
    final = long + short
    
    return final
