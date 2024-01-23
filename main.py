import pandas as pd
pd.set_option('display.max_columns', None)
from scipy.stats import trim_mean, pearsonr
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('netflix_movies.csv')
print(df.shape)
print('\n')
print(df.head(5))
print('\n')
print(df.describe(include='all'))
print('\n')

# print unique rating values
print(df.rating.unique())
# put rating values in right order ['NR' < 'G' < 'PG' < 'PG-13' < 'R']
df.rating = pd.Categorical(df.rating, ['NR', 'G', 'PG', 'PG-13', 'R'], ordered=True)
print(df.rating.unique())

print(df.type.unique())
dummies_df = pd.get_dummies(data=df, columns=['type'])
print(dummies_df.head(3))
print('\n')

# Add column with four budget scopes to  group easier by budgets.

print(f"Minimum budget is equal to: {df['est_budget (USD)'].min()}$")
print(f"Maximum budget is equal to: {df['est_budget (USD)'].max()}$")

budget_scopes = ['small', 'medium', 'large', 'huge']

def sort_budgets(budget):
        if df['est_budget (USD)'].min() <= budget < 2000000:
            return 'small'
        elif 2000000 <= budget < 50000000:
            return 'medium'
        elif 50000000 <= budget < 90000000:
            return 'big'
        else:
            return 'huge'

df['budget_scope'] = df['est_budget (USD)'].apply(lambda x: sort_budgets(x))

print(df.head(5))
print(df.budget_scope.value_counts())
print(round((df.budget_scope.value_counts(normalize=True))*100), 2)
print(df.budget_scope.isnull().sum())
bud_mean = df['est_budget (USD)'].mean()
print(bud_mean)
print(trim_mean(df['est_budget (USD)'], proportiontocut=0.1))
print(df['est_budget (USD)'].median())
budget_iqr = df['est_budget (USD)'].quantile(0.75) - df['est_budget (USD)'].quantile(0.25)
print(f'Budgets IQR = {budget_iqr}')
print(df['est_budget (USD)'].var())
print(df['est_budget (USD)'].std())

# sns.boxplot(data=df, x='est_budget (USD)')
# plt.show()
# plt.clf()

sns.histplot(data=df, x='est_budget (USD)')
plt.axvline(bud_mean, color='r', linestyle='dashed')
plt.ylabel('Netflix productions')
plt.xlabel('Budgets in USD')
plt.show()
plt.clf()

# df.budget_scope.value_counts().plot.pie()
# plt.show()
# plt.close()

print('\n')
print(' CONCLUSION\nBudgets under two million dollars constitute only one percent of the productions.\n'
      'Medium budgets up to 50 milion dolars are most common and contain a half of all productions.\n'
      'Top ten percent of all productions are those with budget over 90 mln dollars. \n'
      'Mean budget is close to 50 mln dollars with median equal to 49,3 mln dollars.\n'
      'Trimming the most extreme data points does not affect the mean value.\n')

# print('Lets dig into empty values \n')
#
# print(df.isnull().sum())
# print(df[df.isnull().any(axis=1)])


# Production types:
print(df.type.unique())

print(df.type.value_counts())
print(df.type.value_counts(normalize=True))

sns.boxplot(data=df, x='type', y='est_budget (USD)')
plt.show()
plt.clf()

movies_budget = df['est_budget (USD)'][df.type == 'Movie']
tvshow_budget = df['est_budget (USD)'][df.type == 'TV Show']

plt.hist(movies_budget, label='Movie', alpha=0.4, density=True, color='red', bins=40)
plt.hist(tvshow_budget, label='Tvshow', alpha=0.4, density=True, color='blue', bins=40)
plt.xlabel('budget - 10 mln USD')
plt.ylabel('Productions')
plt.title('Budgets spread for Movies and TV Shows')
plt.show()
plt.clf()

# sns.histplot(data=df, x=movies_budget, alpha=0.5, common_norm=True)
# sns.histplot(data=df, x=tvshow_budget, alpha=0.5, common_norm=True)
# plt.show()
# plt.clf()

