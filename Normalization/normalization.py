import pandas as pd

messy_data = [
    {
       "order_id": 101,
        "customer_name": "Sam",
        "customer_phone": "0712345678",
        "drink_name": "Latte",
        "drink_size": "Large",
        "drink_price": 45,
        "barista_name": "Alex"  
    },
    {
        "order_id": 102,
        "customer_name": "Sam",
        "customer_phone": "0712345678",
        "drink_name": "Cappuccino",
        "drink_size": "Medium",
        "drink_price": 40,
        "barista_name": "Alex"
    },
    {
         
        "order_id": 103,
        "customer_name": "Jamie",
        "customer_phone": "0798765432",
        "drink_name": "Latte",
        "drink_size": "Small",
        "drink_price": 35,
        "barista_name": "Taylor"
    
    }
]

orders_df = pd.DataFrame(messy_data)
# print(orders_df)

"""""Now I am going to start by looking at customers:
        "customer_name": "Sam",
        "customer_phone": "0712345678",
         "customer_name": "Sam",
        "customer_phone": "0712345678",
        "customer_name": "Jamie",
        "customer_phone": "0798765432",

        I will remove duplicates and add a customers_id column

        I will do the same for drinks , baristas and orders

"""""

def create_tables(orders_df):
    customers_df = orders_df[["customer_name","customer_phone"]].drop_duplicates().reset_index(drop=True)
    customers_df["customer_id"] = customers_df.index + 1

    drinks_df = orders_df[["drink_name","drink_size","drink_price"]].drop_duplicates().reset_index(drop=True)
    drinks_df["drink_id"] = drinks_df.index + 1

    baristas_df = orders_df[["barista_name"]].drop_duplicates().reset_index(drop=True)
    baristas_df["barista_id"] = baristas_df.index + 1



    return customers_df,drinks_df,baristas_df

def normalization(orders_df,customers_df,drinks_df,baristas_df):
   
    orders_normalized = orders_df.merge(customers_df, on=["customer_name", "customer_phone"])
    orders_normalized = orders_normalized.merge(drinks_df, on=["drink_name", "drink_size", "drink_price"])
    orders_normalized = orders_normalized.merge(baristas_df, on="barista_name")

    orders_finalized = orders_normalized[
        ["order_id","customer_id","drink_id","barista_id"]
    ]

    return orders_finalized

customers_df, drinks_df, baristas_df = create_tables(orders_df)

print(normalization(orders_df, customers_df, drinks_df, baristas_df))






