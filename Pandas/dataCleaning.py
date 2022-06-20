"""
Data cleaning means fixing bad data in your data set.
Bad data could be: Empty cells, Data in wrong format, Wrong data & Duplicates
"""

from re import X
import pandas

#load pokemon csv data
pokemonData = pandas.read_csv("pokemon_data.csv")

#remove rows containing null values
removeNullPokemonData = pokemonData.dropna()

print(removeNullPokemonData.to_string())

#filling empty cells
fillNullPokemonData = pokemonData.fillna(128)

print(fillNullPokemonData)

#Fill specific columns
fillType2PokemonData = pokemonData['Type 2'].fillna('Ground')

print(fillType2PokemonData)

#calculate mean 
meanSpeed = pokemonData['Speed'].mean()

print(meanSpeed)

#calculate the median
medianSpeed = pokemonData['Speed'].median()

print(medianSpeed)

#calculate mode speed
modeSpeed = pokemonData['Speed'].mode()[0]

print(modeSpeed)

#checking for duplicated data
print(pokemonData.duplicated())

#removing duplicates
print(pokemonData.drop_duplicates())

#show relationship between columns
print(pokemonData.corr())

#plotting data
import matplotlib.pyplot as plt

pokemonData.plot()

plt.show()

#scatter graph for speed and defence
pokemonData.plot(kind='scatter', x='Speed', y='Defense')

plt.show()

#plotting histogram
pokemonData['Speed'].plot(kind='hist')

plt.show()