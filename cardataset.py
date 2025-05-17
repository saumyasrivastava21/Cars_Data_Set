import pandas as pd
car= pd.read_csv(r"C:\Users\saums\Downloads\file.csv")
print(car.head())
#print(car.shape)
#1.) data cleaning
#find all null value in the dataset. If there is any null value in any column, then fill it with the mean of that colum.
print(car.isnull().sum)
car['Cylinders'].fillna(car['Cylinders'].mean(),inplace = True)
#2.) based on value counts
#check what are diff types of make are there in our dataset,
# and what is count of each make in the data
print(car['Make'].value_counts())
#3.) Instruction(Filtering)
# show all records where origin is Asia or Europe
print(car[car['Origin'].isin(['Asia', 'Europe'])])
#4.) Instruction (Removing all the unwanted records)
#remove all records(rows) where weight is above 4000
print(car[~(car['Weight']> 4000)])
#5.) Instruction (Applying function on a column)
# increase all values of'MPG_City' column by 3
car['MPG_City_plus3'] = car['MPG_City'] + 3
print(car[['MPG_City', 'MPG_City_plus3']].head())