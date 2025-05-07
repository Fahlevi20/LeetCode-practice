import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return person.merge(address,how='left',on='personId')[['firstName','lastName','city','state']]
    

person = {
    'personId': [1, 2],
    'lastName': ['Wang', 'Allen'],
    'firstName': ['Alice', 'Bob'], 

}
personId = pd.DataFrame(person)
address = {
    'addressId': [1, 2],
    'personId': [1, 2],
    'city': ['Seattle', 'Portland'],
    'state': ['WA', 'OR']
}

address_df = pd.DataFrame(address)
print(combine_two_tables(personId, address_df))