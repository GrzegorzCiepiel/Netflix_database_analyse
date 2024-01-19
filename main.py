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
print(dummies_df.head(2))
print('\n')

# Add column with four budget scopes to easier group  by budgets.

print(f"Minimum budget is equal to: {df['est_budget (USD)'].min()}$")
print(f"Maximum budget is equal to: {df['est_budget (USD)'].max()}$")

budget_scopes = ['small', 'medium', 'large', 'huge']

def sort_budgets(budget):
        if budget <= 700000:
            return 'small'
        elif 700000 < budget <= 30000000:
            return 'medium'
        elif 30000000 < budget <= 80000000:
            return 'big'
        else:
            return 'huge'

df['budget_scope'] = df['est_budget (USD)'].apply(lambda x: sort_budgets(x))


print(df.head(30))
