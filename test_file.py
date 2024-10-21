# -*- coding: utf-8 -*-
"""test_file.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qCGJsdyNYfb2TRDxRpOO2kZwg0Q2CGBg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import unittest
import pytest
from data_py import load_data, moving_average_detrend, linear_detrend



def test_moving_average_detrend():
    df, price_data = load_data('data.csv')
    detrended, trend = moving_average_detrend(price_data, window=3)

    assert len(detrended) == len(price_data), "detrended output = input length."
    assert len(trend) == len(price_data), "trend output = input length"
    assert not detrended.isnull().all(), "detrended series should not contain all null values."

def test_linear_detrend():
    df, price_data = load_data('data.csv')
    detrended, trend = linear_detrend(price_data)

    assert len(detrended) == len(price_data), "detrended output = input length."
    assert len(trend) == len(price_data), "trend output = input length."
    assert abs(trend[0] - price_data[0]) < 20, "trend should = input at the start."

