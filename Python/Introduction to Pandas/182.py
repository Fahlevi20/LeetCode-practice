
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person['is_dup']=person.duplicated(subset='email',keep=False)
    return person[person['is_dup']==True][['email']].drop_duplicates()

data = [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']]
person = pd.DataFrame(data, columns=['id', 'email']).astype({'id':'Int64', 'email':'object'})

print(duplicate_emails(person))