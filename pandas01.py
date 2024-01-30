# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:10:38 2024

@author: ubinase
"""

import pandas
file = pandas.read_csv("country_data.csv")
print(file)
print(file.info())
print(file.describe())


diab = pandas.read_csv("diab_data.csv")
print(diab)
print(diab.info())
print(diab.describe())


iris = pandas.read_csv("iris.csv")
print(iris)
print(iris.info())
print(iris.describe())


housing = pandas.read_csv("housing_data.csv")
print(housing)
print(housing.info())
print(housing.describe())


insurance = pandas.read_csv("insurance_data.csv", skiprows=5)
print(insurance)
print(insurance.info())
print(insurance.describe())


#Storing Data
B1 = 30
B2 = 40
B3 = 30
B4 = 49

print(B1)
print(B2)


#Using list
age = [30,40,30,49,22,35,22,46,29,25,39]
print(age)

#List indexes start at 0 which has the value of 30
print(age[0])
print(age[1])
print(age[10])

# This will give an error as there is no value at index 11
print(age[11])

age = [30,40,30,49,22,35,22,46,29,25,39]

# Basic Stats
age = [30,40,30,49,22,35,22,46,29,25,39]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)

# Storing Text
C2 = M
C3 = M
C4 = F

C2 = "M"
C3 = "M"
C4 = "F"
print(C2)
print(C3)
print(C4)

# gender list
gender = ["M","M","F","M","F","F","F","M","M","F","M"]

gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

# country list
country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]

print(country)
print(country[0])
print(country[5])

# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)

# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list) 
print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

# View a certain range of items:
print(my_list[0:3])
      
d = {'key1': 'value1', 'key2': 'value2'}

person = {'name': 'John Doe', 'age': 30, 'address': '123 Main St.'}
print(person['name']) # 'John Doe'
print(person.get('age')) # 30
person['phone'] = '555-555-5555'

import pandas as pd

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)

# Accessing specific columns
print(df['age'])
print(df['gender'])

# Basic statistics
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())

# Filtering data
print(df[df['age'] > 30])

# Slicing rows and columns
print(df[1:4])  # Select rows 1 to 3 and all columns

# Adding a new column
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)

# Removing a column
df.drop(columns=['new_column'], inplace=True)
print(df)

