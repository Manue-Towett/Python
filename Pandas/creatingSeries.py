import pandas

#series in pandas is an equivalent of column in a dataframe
#index can be manipulated into anything other than the default numbering
yearOfBirth = pandas.Series([1987,2015,1996,1998], name="Ages", index = ['a','b','c','d'])

#print all the values
print(yearOfBirth)

#print the maximum value
print(yearOfBirth.max())

#statistics of the numerical data
print(yearOfBirth.describe())

#printing using the personalized labels
print(yearOfBirth['b'])

#key/value objects as a series
calories = pandas.Series({"Monday":430,"Tuesday":520, "Wednesday":450}, name="calories")

print(calories)

#Creating a series using only data from monday and tuesday
newCalories = pandas.Series(calories, index=["Monday", "Tuesday"])

print(newCalories)