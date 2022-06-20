import pandas

#Dataframe in pandas is similar to excel, csv or database table
#Dataframe can be created in pandas as follows
studentsDataframe = pandas.DataFrame({
    "Name": [
        "Emmanuel Towett",
        "Robinson Ali",
        "Jackie Nandy"
    ],
    "RegNo":[
        "J174/4605/2016",
        "J123/5678/2014",
        "T678/7893/2017"
    ],
    "School":[
        "Engineering and Technology",
        "Information Technology",
        "Tourism and Hospitality"
    ]
})

print(studentsDataframe)

#each column in a dataframe is a series
print(studentsDataframe["Name"])

#Locate row with index 1
print(studentsDataframe.loc[1])