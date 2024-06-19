import pandas as pd

east = {'Team': ['Braves', 'Cubs', 'Dodgers', 'Reds', 'Yankees'],
        'Wins': [56, 45, 63, 54, 70]}
print(east)

baseball_df = pd.DataFrame(east)
print(baseball_df.loc[ baseball_df.Team.isin(['Brave', 'Cubs', 'Reds']), :])