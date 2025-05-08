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
print(df.columns)  # This will show you the exact column names

# Display the descriptive statistics
print(df.describe())

# Step 1: Output a summary of each variable to a text file
with open("iris_summary.txt", "w") as f:
    f.write("Dataset Summary:\n")
    f.write(df.describe().to_string())  # Write the descriptive statistics to the text file

# Step 2: Save histograms of each variable to PNG files
# Update the feature names to match what you saw in print(df.columns)
features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
  # Adjust according to your column names

for feature in features:
    plt.figure(figsize=(8, 6))
    sns.histplot(df[feature], kde=True)
    plt.title(f'Histogram of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.savefig(f'{feature}_histogram.png')  # Save histogram as PNG
    plt.close()

# Step 3: Output scatter plot of each pair of variables
for feature1 in features:
    for feature2 in features:
        if feature1 != feature2:
            plt.figure(figsize=(8, 6))
            sns.scatterplot(x=df[feature1], y=df[feature2], hue=df['species'], palette='Set1')
            plt.title(f'Scatter Plot of {feature1} vs {feature2}')
            plt.xlabel(feature1)
            plt.ylabel(feature2)
            plt.savefig(f'{feature1}_vs_{feature2}_scatter.png')  # Save scatter plot as PNG
            plt.close()

# Step 4: Additional analysis
# Compute correlation matrix
correlation_matrix = df[features].corr()

# Plot the correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Features')
plt.show()

# Box plots of each feature grouped by species
for feature in features:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='species', y=feature, data=df, palette='Set2')
    plt.title(f'Box Plot of {feature} by Species')
    plt.savefig(f'{feature}_boxplot_by_species.png')  # Save boxplot as PNG
    plt.close()



































