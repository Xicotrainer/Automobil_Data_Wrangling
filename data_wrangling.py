import pandas as pd
import matplotlib.pylab as plt
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
print(df.sample(8))

# They will replaced by "NaN"
df.replace("?", np.nan, inplace = True)
print(df.sample(8))

# Identify the number of missing values
missing_data = df.isnull()
print(missing_data.sample(8))
for column in missing_data.columns.values.tolist():
	print(column)
	print(missing_data[column].value_counts(),"\n")

# Replace by mean
forChanging = ["normalized-losses", 
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
print(df.sample(8))
print(df.dtypes)