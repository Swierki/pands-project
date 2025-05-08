# Fisher’s Iris data set Project
# Objectives
# Iris Species Similarity Index
# A. Fisher in 1936, it contains measurements of iris flowers from three different species: Iris setosa, Iris versicolor, and Iris virginica. Each sample includes four features:



# Author: Lukasz Swierkowski

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('C:/Users/luke_/Documents/iris.csv')

# Strip any leading/trailing whitespace in column names
df.columns = df.columns.str.strip()

# Print the column names to verify
print(df.columns)

# Display the descriptive statistics
print(df.describe())

# Step 1: Output a summary of each variable to a text file
with open("iris_summary.txt", "w") as f:
    f.write("Dataset Summary:\n")
    f.write(df.describe().to_string())  # Write the descriptive statistics to the text file





# This project compares similarities in the  index between the three Iris species by:
# Measuring how close their average feature vectors are.
# Using Euclidean distance and cosine similarity between species centroids
# Visualizing similarity using a dendrogram or heatmap.






























