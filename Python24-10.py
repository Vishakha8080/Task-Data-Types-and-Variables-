import numpy as np

numbers = [1, 2, 3, 4, 5]
arr = np.array(numbers)
print("Sum:", np.sum(arr))
print("Product:", np.prod(arr))

############################################################################

import numpy as np

arr = np.arange(9).reshape(3, 3)
print(arr)

############################################################################

import numpy as np

data = np.array([10, 20, 30, 40, 50])
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))


############################################################################

import numpy as np

def sort_array(lst):
    arr = np.array(lst)
    return np.sort(arr)

print(sort_array([3, 1, 4, 2]))


############################################################################


import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Row sums:", np.sum(matrix, axis=1))
print("Column sums:", np.sum(matrix, axis=0))

############################################################################

import numpy as np

arr = np.random.rand(5, 5)
print("Array:\n", arr)
print("Max:", np.max(arr))
print("Min:", np.min(arr))

############################################################################

import numpy as np

def square_elements(arr):
    return np.square(arr)

print(square_elements(np.array([1, 2, 3, 4])))

############################################################################

import numpy as np

arr = np.array([1, 2, 3])
print("Dot Product:", np.dot(arr, arr))

############################################################################

import numpy as np

matrix = np.array([[4, 7], [2, 6]])
inverse = np.linalg.inv(matrix)
print("Inverse:\n", inverse)

############################################################################

import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
print("Transpose:\n", arr.T)

############################################################################

import pandas as pd

df = pd.read_csv("students.csv")
print("Average Age:", df["Age"].mean())

############################################################################

import pandas as pd

dates = pd.date_range("2025-01-01", periods=10)
series = pd.Series(dates)
filtered = series[(series >= "2025-01-03") & (series <= "2025-01-07")]
print(filtered)

############################################################################

import pandas as pd

dates = pd.date_range("2025-01-01", periods=10)
series = pd.Series(dates)
filtered = series[(series >= "2025-01-03") & (series <= "2025-01-07")]
print(filtered)

############################################################################

import pandas as pd

df = pd.read_csv("students.csv")
print("Max values:\n", df.max())
print("Min values:\n", df.min())

############################################################################

import pandas as pd

df = pd.read_csv("students.csv")
print("Max values:\n", df.max())
print("Min values:\n", df.min())

############################################################################

import pandas as pd

def sort_dataframe(df):
    return df.sort_values(by="Age")

df = pd.read_csv("students.csv")
print(sort_dataframe(df))

############################################################################

import pandas as pd

df = pd.read_csv("students.csv")
filtered = df[df["Marks"] > 85]
print(filtered)

############################################################################

import pandas as pd

df = pd.read_csv("students.csv")
print("Total Marks:", df["Marks"].sum())

############################################################################

import pandas as pd

df = pd.read_csv("students.csv")
df["Result"] = ["Pass" if m >= 50 else "Fail" for m in df["Marks"]]
print(df)

############################################################################

import pandas as pd

data = {
    "Dept": ["IT", "IT", "CS", "CS"],
    "Marks": [85, 90, 80, 95]
}
df = pd.DataFrame(data)

print(df.groupby("Dept")["Marks"].mean())

############################################################################

import pandas as pd

df = pd.read_json("data.json")
print(df[df["age"] > 20])

############################################################################

import pandas as pd

df = pd.read_csv("students.csv")
print(df.T)

