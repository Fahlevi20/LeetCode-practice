import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(students)
    select_student=df[df['student_id'] == 101][['name','age']]
    print(select_student)

    return select_student

data = {
    'student_id': [101, 53,128,3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13,10,6,11]
    }

selectData(data)