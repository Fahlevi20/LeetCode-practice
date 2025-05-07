import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df=orders

    counts=df.groupby('customer_number')
    first_large=df.sort_values(by='customer_number',ascending=False).iloc[[0]]


    return first_large[['customer_number']]
    

data = {
    'customer_number': [1, 2, 3, 4],
    'order_number': [1, 2, 3, 3]
}
largest_orders_df = pd.DataFrame(data)
print(largest_orders(largest_orders_df))