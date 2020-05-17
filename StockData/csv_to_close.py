import pandas as pd

def csv_to_close(csv_filepath, field_names):
    """Reads in data from a csv file and produces a DataFrame with close data.
    
    Parameters
    ----------
    csv_filepath : str
        The name of the csv file to read
    field_names : list of str
        The field names of the field in the csv file

    Returns
    -------
    close : DataFrame
        Close prices for each ticker and date
    """
    
    price_df = pd.read_csv(csv_filepath, names=field_names)
    
    close_prices = price_df.pivot(index='date', columns='ticker', values='close')    
    
    return close_prices
