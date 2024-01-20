import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv('netflix_movies.csv')
print(df.head(5))

# print unique rating values
print(df.rating.unique())
# put rating values in right order ['NR' < 'G' < 'PG' < 'PG-13' < 'R']
df.rating = pd.Categorical(df.rating, ['NR', 'G', 'PG', 'PG-13', 'R'], ordered=True)
print(df.rating.unique())

print(df.type.unique())
dummies_df = pd.get_dummies(data=df, columns=['type'])
print(dummies_df.head(3))
print('\n')

# Add column with four budget scopes to easier group  by budgets.

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
print(df.budget_scope.isnull().sum())


# print('Lets dig into empty values \n')
#
# print(df.isnull().sum())
# print(df[df.isnull().any(axis=1)])