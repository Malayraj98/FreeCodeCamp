import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('medical_examination.csv')

df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'alco', 'active', 'smoke'])

g = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count')
g.set_axis_labels('variable', 'total')
g.set_titles('{col_name} {col_var}')
plt.show()

df_cleaned = df[(df['ap_lo'] <= df['ap_hi']) &
                (df['height'] >= df['height'].quantile(0.025)) &
                (df['height'] <= df['height'].quantile(0.975)) &
                (df['weight'] >= df['weight'].quantile(0.025)) &
                (df['weight'] <= df['weight'].quantile(0.975))]

corr_matrix = df_cleaned.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.1f', cmap='coolwarm', linewidths=.5, mask=pd.np.triu(corr_matrix))
plt.title('Correlation Matrix')
plt.show()
