# -*- coding: utf-8 -*-
"""TreeData.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hoj-qITWmXlKJ1vOf2-vdSlVj80xrQtg
"""

#Data_Cleaning

mask = ((tree_census_subset['status'] == 'Stump') | (tree_census_subset['status'] == 'Dead'))

tree_census_subset.loc[mask] = tree_census_subset.loc[mask].fillna('Not Applicable')

tree_census_subset[tree_census_subset['status']=='Stump']

tree_census_subset.isna().sum()

tree_census_subset[tree_census_subset['health'].isna()]

tree_census_subset[tree_census_subset['sidewalk'].isna()]

tree_census_subset[tree_census_subset['spc_latin'].isna()]

tree_census_subset[tree_census_subset['problems'].isna()]

tree_census_subset['problems'].fillna('None', inplace=True)
tree_census_subset['health'].fillna('Good', inplace=True)
tree_census_subset['spc_latin'].fillna('No Observation', inplace=True)
tree_census_subset['sidewalk'].fillna('NoDamage', inplace=True)

tree_census_subset.isna().sum()

big_trees = tree_census_subset[(tree_census_subset['tree_dbh']>60) | (tree_census_subset['stump_diam']>60)]
big_trees

tree_census_subset = tree_census_subset[(tree_census_subset['tree_dbh']<=60) | (tree_census_subset['stump_diam']<=60)]
tree_census_subset

tree_census_subset_alive = tree_census_subset[tree_census_subset['status']=='Alive']
tree_census_subset_dead_or_Stump = tree_census_subset[(tree_census_subset['status']=='Dead') | (tree_census_subset['status']=='Stump')]

stats_alive = tree_census_subset_alive.groupby('spc_latin')['tree_dbh'].describe().reset_index()[['spc_latin','25%','75%']]
stats_alive

tree_census_subset_alive = tree_census_subset_alive.merge(stats_alive, on='spc_latin', how='left')
tree_census_subset_alive

mask = tree_census_subset_alive['tree_dbh']<tree_census_subset_alive['25%']
tree_census_subset_alive.loc[mask,'tree_dbh'] = tree_census_subset_alive['25%']

mask = tree_census_subset_alive['tree_dbh']>tree_census_subset_alive['75%']
tree_census_subset_alive.loc[mask,'tree_dbh'] = tree_census_subset_alive['75%']

tree_census_subset_alive