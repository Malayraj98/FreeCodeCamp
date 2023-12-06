import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

df_cleaned = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    plt.figure(figsize=(14, 6))
    plt.plot(df_cleaned.index, df_cleaned['value'], color='red', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.grid(True)
    
    plt.savefig('line_plot.png')
    return plt.gca()

def draw_bar_plot():

    df_bar = df_cleaned.copy()
    df_bar['Month'] = df_bar.index.month
    df_bar['Year'] = df_bar.index.year
    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean().unstack()

    ax = df_bar.plot(kind='bar', figsize=(12, 10), legend=True)
    plt.title('Average Page Views by Year and Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=list(calendar.month_abbr)[1:])

    plt.savefig('bar_plot.png')
    return plt.gca()

def draw_box_plot():

    df_box = df_cleaned.copy()
    df_box.reset_index(inplace=True)
    df_box['Month'] = df_box['date'].dt.strftime('%b')
    df_box['Year'] = df_box['date'].dt.year

    plt.figure(figsize=(15, 5))
    plt.subplot(1, 2, 1)
    sns.boxplot(x='Year', y='value', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    plt.subplot(1, 2, 2)
    sns.boxplot(x='Month', y='value', data=df_box, order=list(calendar.month_abbr)[1:])
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    plt.savefig('box_plot.png')
    return plt.gca()