import pandas as pd

def remove_duplicates(df):
    df = df.drop_duplicates().reset_index(drop=True)
    return df

# Example
data = {'A': [1, 2, 2, 3], 'B': [5, 6, 6, 7]}
df = pd.DataFrame(data)
print(remove_duplicates(df))

################################################################################

import pandas as pd
from sklearn.impute import SimpleImputer

# Read CSV
df = pd.read_csv("data.csv")

# Handle missing values
imputer = SimpleImputer(strategy='mean')
df[df.select_dtypes(include='number').columns] = imputer.fit_transform(df.select_dtypes(include='number'))

print(df.head())

################################################################################

import pandas as pd

def encode_text(df, column_name):
    encoded_df = pd.get_dummies(df, columns=[column_name])
    return encoded_df

# Example
df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green']})
print(encode_text(df, 'Color'))

################################################################################

import pandas as pd

def z_score_normalization(df):
    numeric_df = df.select_dtypes(include='number')
    df[numeric_df.columns] = (numeric_df - numeric_df.mean()) / numeric_df.std()
    return df

# Example
df = pd.DataFrame({'A':[10,20,30],'B':[5,10,15]})
print(z_score_normalization(df))

################################################################################

import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame({'A':[1,2,3,4], 'B':[10,20,30,40]})

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

standardized_df = pd.DataFrame(scaled_data, columns=df.columns)
print(standardized_df)

################################################################################

import pandas as pd
from scipy.stats.mstats import winsorize

# Read JSON file
df = pd.read_json("data.json")

# Handle outliers in the 'Salary' column
df['Salary_winsorized'] = winsorize(df['Salary'], limits=[0.05, 0.05])

print(df)

################################################################################

import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif

def feature_selection(X, y, k=2):
    selector = SelectKBest(score_func=f_classif, k=k)
    X_new = selector.fit_transform(X, y)
    selected_features = X.columns[selector.get_support()]
    return selected_features

# Example
X = pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8],'C':[1,3,5,7]})
y = [0,1,0,1]
print(feature_selection(X, y))

################################################################################

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

df = pd.read_csv("customers.csv")

# Handle missing values
imputer = SimpleImputer(strategy='mean')
df[df.select_dtypes(include='number').columns] = imputer.fit_transform(df.select_dtypes(include='number'))

# Scale features
scaler = StandardScaler()
df[df.select_dtypes(include='number').columns] = scaler.fit_transform(df.select_dtypes(include='number'))

print(df.head())

################################################################################

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data.csv")

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.select_dtypes(include='number'))

pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(pca_data, columns=['PC1', 'PC2'])
print(pca_df.head())

################################################################################
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer

def discretize_data(df, column_name, bins=3):
    discretizer = KBinsDiscretizer(n_bins=bins, encode='ordinal', strategy='uniform')
    df[column_name + '_binned'] = discretizer.fit_transform(df[[column_name]])
    return df

# Example
df = pd.DataFrame({'Age':[10,20,30,40,50]})
print(discretize_data(df, 'Age', bins=3))

################################################################################

################################################################################
