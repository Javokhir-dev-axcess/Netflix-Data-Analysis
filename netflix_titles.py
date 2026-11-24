import pandas as pd
import matplotlib.pyplot as plt
try:
    df = pd.read_csv('netflix_titles.csv')
    print('Dataset found. ')
except FileNotFoundError:
    print('File Not Found.')
    exit()
# Movie vs TV Shows count  
counts = df['type'].value_counts()
print('Movie vs TV Shows: ', counts) 
# Top 10 countries: dropna() - removes blocks with NaN values; value_counts() - counts 
top_countries = df['country'].dropna().value_counts().head(10)
print('Top 10 countries: ', top_countries)
# Contents released after 2000
yearly_releases = (
    df.loc[df['release_year'] >= 2000, 'release_year']
    .value_counts()
    .sort_index()
)
#Visualization part - Matplotlib
#Movies vs TV Shows (Bar Chart)
plt.figure('Content Type', figsize = (7, 5))
plt.bar(counts.index, counts.values, color = ['red', 'blue'])
plt.title('Netflix: Movies vs TV Shows')
plt.xlabel('Type')
plt.ylabel('Count')
plt.savefig('Netflix_F1')
plt.show()

#Top 10 countries who are leading in cinema industry
plt.figure('Top countries', figsize = (7, 5))
plt.barh(top_countries.index[: : -1], top_countries.values[: : -1], color = 'green')
plt.title('Top 10 Content Creating Countries in Netflix')
plt.xlabel('Amount')
plt.tight_layout()
plt.savefig('Netflix_F2')
plt.show()

#Releases after 2000
plt.figure('Yearly Growth', figsize=(7, 5))
plt.plot(yearly_releases.index, yearly_releases.values, color = 'gray')
plt.title('Netflix Contents after 2000s')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.savefig('Netflix_F3')
plt.show()

#Summary
# 1. Movies make up a significantly larger share of the catalog than TV Shows.
# 2. The United States leads by a wide margin in content count, followed by markets like India and the UK.
# 3. Releases grew rapidly after 2000, showing a sharp surge around 2015-2018 before leveling off.

