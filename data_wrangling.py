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

# Identify the proportion of missing values
missing_data = df.isnull()
print(missing_data.sample(8))
for column in missing_data.columns.values.tolist():
	print(column)
	print(missing_data[column].value_counts(),"\n")
