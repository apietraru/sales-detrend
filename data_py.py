# -*- coding: utf-8 -*-
"""data_py.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1leuXJ2CRzxkcrmv7Gb-UDlY5STLbOiF9
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import unittest


# Load the data
file_path = 'data.csv'
df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
price_data = df['Sales']


def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df, df['Sales']

#remove trend using moving average
def moving_average_detrend(data, window=30):
    trend = data.rolling(window=window).mean()
    detrended = data - trend
    return detrended, trend
detrended_ma, ma_trend = moving_average_detrend(price_data)

#remove trend using linear regression
def linear_detrend(data):
    X = np.arange(len(data)).reshape(-1, 1)
    model = LinearRegression().fit(X, data)
    trend = model.predict(X)
     # Adjust the trend so that the first value matches the first value of the data
    adjustment = data.iloc[0] - trend[0]
    trend = trend + adjustment  # Shift the trend up or down
    detrended = data - trend
    return detrended, trend
detrended_linear, linear_trend = linear_detrend(price_data)

#plot original data and detrended data
plt.figure(figsize=(10, 8))
plt.subplot(3, 1, 1)
plt.plot(df.index, price_data, label='orig data')
plt.plot(df.index, ma_trend, label='average trend', linestyle='--')
plt.plot(df.index, detrended_ma, label='detrended', linestyle='-.')
plt.title('MA. Detrending')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(df.index, price_data, label='orig Data')
plt.plot(df.index, linear_trend, label='linear Trend', linestyle='--')
plt.plot(df.index, detrended_linear, label='detrended', linestyle='-.')
plt.title('Linear Detrending')
plt.legend()

plt.tight_layout()
plt.show()

class TestDetrendingFunctions(unittest.TestCase):

    def setUp(self):
        """ set up sample data for testing """
        self.sample_data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_moving_average_detrend(self):
        """ test moving average detrending """
        detrended, trend = moving_average_detrend(self.sample_data, window=3)

        # check if right length
        self.assertEqual(len(detrended), len(self.sample_data))
        self.assertEqual(len(trend), len(self.sample_data))

        # Ensure there are no NaN values after detrending (except for the start due to rolling)
        self.assertFalse(detrended.isna().all())

    def test_linear_detrend(self):
        """ test linear regression detrending """
        detrended, trend = linear_detrend(self.sample_data)

        # check if right length
        self.assertEqual(len(detrended), len(self.sample_data))
        self.assertEqual(len(trend), len(self.sample_data))

        # check same start
        self.assertAlmostEqual(trend[0], self.sample_data[0], delta=0.5)

unittest.main(argv=[''], exit=False)




