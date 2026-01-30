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
print(orders_df)