import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('fifa21.csv', low_memory=False)
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', None)

df['Weight'] = df['Weight'].str.replace('lbs', '').apply(int)
split_df = df['Height'].str.split('\'', expand=True)
split_df.columns = ['foot', 'inch']
split_df['foot'] = split_df['foot'].apply(int)*30.48
split_df['inch'] = split_df['inch'].str.replace('\"', '').apply(int)*2.54
df['Height'] = split_df['foot'] + split_df['inch']

for column in df.columns:
    if df[column].dtype == object:
        df[column] = df[column].str.replace('\n',' ')

df['Joined'] = pd.to_datetime(df['Joined'], format="%b %d, %Y")
filt = pd.to_datetime('today') - df['Joined'] > pd.to_timedelta('3652.5 days')
#print(df.loc[filt, 'LongName'])

plt.figure(figsize=(10, 6))
plt.scatter(df['Value'], df['Wage'], alpha=0.5)
plt.title('Scatter Plot of Player Value vs. Wage')
plt.xlabel('Player Value (€)')
plt.ylabel('Wage (€ per week)')
plt.xscale('log')
plt.yscale('log')
#plt.show()

df.drop(columns = ['photoUrl','playerUrl'], inplace= True)

print(df.columns)