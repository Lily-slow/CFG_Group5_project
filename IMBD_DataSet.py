import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)

basics_df = pd.read_csv('title.basics.tsv.gz', sep='\t', low_memory=False)
ratings_df = pd.read_csv('title.ratings.tsv.gz', sep='\t', low_memory=False)
names_df = pd.read_csv('name.basics.tsv.gz', sep='\t', low_memory=False)


print(basics_df.shape)
print(basics_df.head(10))
print(ratings_df.shape)
print(ratings_df.head(10))
print(names_df.shape)
print(names_df.head(10))
print(names_df.columns)

# # Merge the two dataframes on the 'tconst' column
# merged_df = pd.merge(basics_df, ratings_df, on='tconst', how='inner')
#
# # Get summary statistics for the numerical columns
# print(merged_df.describe())
#
# # Get the top 10 most common genres
# print(merged_df['genres'].value_counts().head(10))
#
# # Get the mean rating for each genre
# print(merged_df.groupby('genres')['averageRating'].mean())
#
# # Merge the names dataframe with the merged_df on the 'nconst' column
# names_merged_df = pd.merge(names_df, merged_df, on='nconst', how='inner')
#
# # Get the top 10 most common professions
# print(names_merged_df['primaryProfession'].value_counts().head(10))
#
# # Get the mean rating for each profession
# print(names_merged_df.groupby('primaryProfession')['averageRating'].mean())
#
#
# filtered_df = merged_df.loc[(merged_df['startYear'].str.isnumeric()) & (merged_df['primaryTitle'].str.contains('contagion', case=False, regex=False))]
# filtered_df.loc[:,'startYear'] = filtered_df['startYear'].astype('float')
# filtered_df = filtered_df[(filtered_df['startYear'] >= 2019) & (filtered_df['startYear'] <= 2022)]
#
# plt.plot(filtered_df['startYear'], filtered_df['averageRating'], 'o-')
# plt.xlabel('Year')
# plt.ylabel('Average Rating')
# plt.title('Contagion Ratings Over Time')
# plt.show()

