# sales
i. This project aims to detrend a time series dataset of daily prices using the moving average method. By applying a moving average to smooth the data, the trend is identified and removed, leaving the underlying fluctuations in the data more apparent. The original data and the detrended data are then plotted for comparison.

ii. Libraries: pandas, mathplotlib
    Methods: Moving average detrending- This method calculates the average of the data over a defined window. The moving average represents the trend in the data, and subtracting it from the original values showes the detrended data. This helps in highlighting short-term fluctuations in the data by removing long-term trends.
             Linear detrend - Removes a consistent upward or downward trend by fitting a straight line to the data and subtracting it, leaving only the fluctuations or deviations from the trend.
iii.Data needed: csv file with date and prices

iv.The project will produce a plot showing: the original data (daily prices),the moving average trend, the detrended data
This visualization will make it clear how much the trend affects the data and what remains when the trend is removed, helping in understanding the natural variations in the dataset


-Ana Pietraru 5933889
