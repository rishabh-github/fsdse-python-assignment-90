import pandas as pd


def equal_operator(array1, array2):
    ds1 = pd.Series(array1)
    ds2 = pd.Series(array2)
    ds = ds1 == ds2
    return ds


def greater_than_operator(array1, array2):
    ds1 = pd.Series(array1)
    ds2 = pd.Series(array2)
    ds = ds1 > ds2
    return ds


def less_than_operator(array1, array2):
    ds1 = pd.Series(array1)
    ds2 = pd.Series(array2)
    ds = ds1 < ds2
    return ds
