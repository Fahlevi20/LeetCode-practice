import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee,left_on='managerId', right_on='id', how='inner')
    
    return df[df['salary_x']> df['salary_y']][['name_x']].rename(columns={'name_x':'Employee'})


    


data = [[1, 'Joe', 70000, 3], [2, 'Henry', 80000, 4], [3, 'Sam', 60000, None], [4, 'Max', 90000, None]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'managerId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'managerId':'Int64'})
print(find_employees(employee))