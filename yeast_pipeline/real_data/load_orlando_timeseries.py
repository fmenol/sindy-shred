import pandas as pd
import numpy as np

def load_orlando_timeseries(filepath):
    """
    Load yeast time series data from Orlando et al. 2008.

    Parameters
    ----------
    filepath : str
        Path to the .tsv file

    Returns
    -------
    time : ndarray of shape [T]
    gene_expr : ndarray of shape [T, G]
    gene_names : list of str
    """
    df = pd.read_csv(filepath, sep='\t')
    time = df.iloc[:, 0].values
    gene_expr = df.iloc[:, 1:].values
    gene_names = df.columns[1:].tolist()

    return time, gene_expr, gene_names
