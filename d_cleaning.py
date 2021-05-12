import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Automobile data set has wenty-six atributes/columns
headers = ["symboling",
			"normalized-losses",
			"make","fuel-type",
			"aspiration", 
			"num-of-doors",
			"body-style",
			"drive-wheels",
			"engine-location",
			"wheel-base",
			"length","width",
			"height",
			"curb-weight",
			"engine-type",
        	"num-of-cylinders",
        	"engine-size",
        	"fuel-system",
        	"bore","stroke",
        	"compression-ratio",
        	"horsepower",
        	"peak-rpm",
        	"city-mpg",
        	"highway-mpg",
        	"price"]

# Just read the file in the same folder 
df = pd.read_csv("data.csv", names = headers)

# There are many missing values
print(df.sample(8), "\n")

# They will replaced by "NaN"
df.replace("?", np.nan, inplace = True)

# Identify the number of missing values
missing_data = df.isnull()
print(missing_data.sample(8), "\n")
for column in missing_data.columns.values.tolist():
	print(column)
	print(missing_data[column].value_counts(),"\n")

# Replace by mean
forChanging = [ "normalized-losses", 
				"bore",
				"stroke",
				"horsepower",
				"peak-rpm"]

for atribute in forChanging:
	avg = df[atribute].astype("float").mean(axis = 0)
	df[atribute].replace(np.nan, avg, inplace = True)
	print("Average {}: {}".format(atribute, avg))

# Replace by most common type
mode = df["num-of-doors"].value_counts().idxmax()
df["num-of-doors"].replace(np.nan, mode, inplace = True)

# Drop every row without price and actualize the index
df.dropna(subset = ["price"], axis = 0, inplace = True)
df.reset_index(drop = True, inplace = True)

# Now, the data has no missing values
print("\n", df.sample(8), "\n")

# We make sure the data has the correct data format
print(df.dtypes, "\n")

# Actualize words to numbers
forChanging = [ "normalized-losses", 
				"bore",
				"stroke",
				"price",
				"peak-rpm"]

for atribute in forChanging:
	df[atribute]= df[atribute].astype("float")

# Data Standarization (International System of Units)
df["city-L/100km"] = 235 / df ["city-mpg"]
df["highway-L/100km"] = 235 / df["highway-mpg"]
df.drop(columns = ["city-mpg","highway-mpg"])

print(df.sample(8), "\n")

# Data Normalization (between the maximum)
forChanging = [ "length",
				"width",
				"height"]

for atribute in forChanging:
	df[atribute] = df[atribute] / df[atribute].max()
print(df[forChanging].sample(8), "\n")


# Binnig (Low-Mid-High meter)
df["horsepower"] = df["horsepower"].astype(int, copy = True)

plt.hist(df["horsepower"], bins = 3)
plt.xlabel("Horsepower")
plt.ylabel("Count")
plt.title("Horsepower bins")
plt.show()

# Data actualization	
horsepower_bins = np.linspace(df["horsepower"].min(), df["horsepower"].max(), 4)
group_names = {"Low", "Medium", "Hight"}
df["horsepower-binned"] = pd.cut(df["horsepower"], horsepower_bins, labels = group_names, include_lowest = True)

print(df[["horsepower", "horsepower-binned"]].sample(8), "\n")
print(df["horsepower-binned"].value_counts(), "\n")

# Dummy variables (1-0 stages for regresion models)
dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.rename(columns = { 'gas':'fuel-type-gas', 
									'diesel':'fuel-type-diesel'},
									 inplace = True)

df = pd.concat([df, dummy_variable_1], axis = 1)
df.drop("fuel-type", axis = 1, inplace = True)

dummy_variable_2 = pd.get_dummies(df["aspiration"])
dummy_variable_2.rename(columns = { 'std':'aspiration-std',
									'turbo': 'aspiration-turbo'}, 
									inplace = True)

df = pd.concat([df, dummy_variable_2], axis = 1)
df.drop("aspiration", axis = 1, inplace = True)

print(df.sample(8), "\n")

#df.to_csv('clean_data.csv')

