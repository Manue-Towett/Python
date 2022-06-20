import pandas

#loading data to pandas
pokemonData = pandas.read_csv('pokemon_data.csv')

#print all the data
print(pokemonData)

#print the first five rows
print(pokemonData.head(5))

#print last five rows
print(pokemonData.tail(5))

#checking how python interpreted data in each column
print(pokemonData.dtypes)

#writing pokemon data into excel sheet
#pokemonData.to_excel('pokemon.xlsx', sheet_name='pokemon', index=False)

#read data from excel file
pokemonData = pandas.read_excel('pokemon.xlsx')

print(pokemonData)

#obtain summary of the dataframe
print(pokemonData.info())

#locate row with index 1
print(pokemonData.loc[1])

#locate row with index 1, 2 and 3
print(pokemonData.loc[[1,2,3]])

#locate rows in a range
print(pokemonData.loc[1:4])

#to_string() method is used to print all data
print(pokemonData.to_string())

#check max rows printed
print(pandas.options.display.max_rows)

#load json data
calories = pandas.read_json("time.json")

print(calories)