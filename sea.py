import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')

plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.75, label='Actual Data')

slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

years_future = range(1880, 2051)
line_fit_all_data = slope * years_future + intercept
plt.plot(years_future, line_fit_all_data, color='red', label='Line of Best Fit (All Data)')

df_recent_data = df[df['Year'] >= 2000]

slope_recent, intercept_recent, _, _, _ = linregress(df_recent_data['Year'], df_recent_data['CSIRO Adjusted Sea Level'])

line_fit_recent_data = slope_recent * years_future + intercept_recent
plt.plot(years_future, line_fit_recent_data, color='green', label='Line of Best Fit (Recent Data)')

plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

plt.savefig('sea_level_plot.png')
plt.show()