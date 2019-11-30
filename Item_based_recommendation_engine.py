# Loading the required libraries
import pandas as pd # Data processing
import numpy as np # Linear Algebra
import timeit as t

# Loading the dataset
data1 = pd.read_csv("file:///D:/NMIMS/SEM-3/SC-5/lastfm-matrix-germany.csv")

# Preview Data
data1.head()
data1.tail()

# Rows and columns in the dataframe
data1.shape

# Column names in the dataset
list(data1)

# Database type
data1.info()

# Checking if any columns contain any missing data 
data1.isnull().sum()

# Summary of each column ie mean, median, mode etc
data1.describe(include='all')

# Item based Recommendation Engine
# Count of songs that a particular user listen
data1['sum1'] = data1.iloc[:,1::].sum(axis = 1)

# Sorting the user according to the songs listen by them
data1 = data1.sort_values(by = ['sum1'], ascending= False)

# Removing the User column from the dataset
rating_data = data1.loc[:,data1.columns != 'user']

# Small exercise to understand how to find the cosine similarity between the songs 'a perfect circle' & 'ac/dc'
xxy = (data1['a perfect circle']*data1['ac/dc'])
x = data1['a perfect circle']**2
y = data1['ac/dc']**2
cos_sim = xxy.sum()/np.sqrt(x.sum()*y.sum()) # Cosine similarity between 'a perfect circle' & 'ac/dc'


# Extending the above exercise of finding cosine similarity to the whole dataset
start = t.timeit() # Time when the loop starts
item_similarity_matrix = pd.DataFrame(index= rating_data.columns, columns= rating_data.columns)
for i in range(0,len(data1.columns)-1):
    for j in range(0,len(data1.columns)-1):
        a = rating_data.iloc[:,i]*rating_data.iloc[:,j]
        a1 = rating_data.iloc[:,i]**2
        b1 = rating_data.iloc[:,j]**2
        item_similarity_matrix.iloc[i,j] = a.sum()/np.sqrt(a1.sum()*b1.sum())
end=t.timeit() # Time when the loop ends
print(end - start) # Print the time required for the above loop to run


# Create a placeholder items for closes neighbours to an item
item_neighbour = pd.DataFrame(index = item_similarity_matrix.columns, columns= range(1,11))


# Loop through our similarity dataframe and fill in neighbouring item names
for i in range(0,len(item_similarity_matrix.columns)):
    item_neighbour.iloc[i,:10] = item_similarity_matrix.iloc[0:,i].sort_values(ascending=False)[:10].index[:10]



# Performing the same above exercise using lists
start = t.timeit() # Time when the loop starts
item_similarity_matrix = []
for i in range(0, len(data1.columns)-1):
    for i in range(0, len(data1.columns)-1):
        a = rating_data.iloc[:,i]*rating_data.iloc[:,j]
        a1 = rating_data.iloc[:,i]**2
        b1 = rating_data.iloc[:,j]**2
        cos = a.sum()/np.sqrt(a1.sum()*b1.sum())
        item_similarity_matrix.append(cos)
end = t.timeit() # Time when the loop ends
print(end-start) # Print the time required for the above loop to run

