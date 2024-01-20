import pandas as pd

def CreateDataFrame(student_data: list[list[int]]) -> pd.DataFrame: ##Right Arrow for makesure the data type still in DataFrame
    df = pd.DataFrame(student_data, columns=['student_id','age'])
    print(df)

    return df


student_data=[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

CreateDataFrame(student_data)