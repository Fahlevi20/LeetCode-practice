import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df=orders

    # counts=df.groupby('customer_number')
    count=df.groupby(by="customer_number").size().reset_index(name='order_count')
    print(count)
    first_large=count.sort_values(by='order_count',ascending=False).head(1)
    return (first_large[['customer_number']])


    # return first_large[['customer_number']]
    

data = {
    'customer_number': [1, 2,3,3 ],
    'order_number': [1, 2, 3, 3.4]
}
largest_orders_df = pd.DataFrame(data)
print(largest_orders(largest_orders_df))