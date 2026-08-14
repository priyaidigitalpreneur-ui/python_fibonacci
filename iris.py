from ucimlrepo import fetch_ucirepo 
import pandas as df
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data
X = iris.data.features 
y = iris.data.targets 
  
# metadata
print(iris.metadata) 
  
# variable information
print(iris.variables) 

# total number of different flowers
total_different_flowers = len(set(y.values.flatten()))
print(f'Total different flowers in the dataset: {total_different_flowers}')

# total number of rows and columns
rows, columns = X.shape 
print(f'Total number of rows in the dataset: {rows}')
print(f'Total number of columns in the dataset: {columns}')

# names of different flowers
flower_names = set(y.values.flatten())
print(f'The different flowers in the dataset are: {flower_names}')
