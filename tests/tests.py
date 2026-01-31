import unittest
from Normalization.normalization import *
import pandas



""""    customer_name": "Sam",
        "customer_phone": "0712345678",
        "drink_name": "Latte",
        "drink_size": "Large",
        "drink_price": 45,
        "barista_name": "Alex" 
        """

class TestCase(unittest.TestCase):
    def test_unique_customers(self):
        customers_df,drinks_df,baristas_df = create_tables(orders_df)
        self.assertFalse(customers_df.duplicated(subset=["customer_name","customer_phone"]).any())
        self.assertFalse(drinks_df.duplicated(subset=["drink_name","drink_size","drink_price"]).any())
        self.assertFalse(baristas_df.duplicated(subset=["barista_name"]).any())


    def test_no_missing_ids(self):
        self.assertFalse(orders_finalized["customer_id"].isnull().any())
        self.assertFalse(orders_finalized["drink_id"].isnull().any())
        self.assertFalse(orders_finalized["barista_id"].isnull().any())

    def test_id_exist_in_parent_table(self):
        self.assertTrue(set(orders_finalized["customer_id"]).issubset(set(customers_df["customer_id"])))
        self.assertTrue(set(orders_finalized["drink_id"]).issubset(set(drinks_df["drink_id"])))
        self.assertTrue(set(orders_finalized["barista_id"]).issubset(set(baristas_df["barista_id"])))

if __name__ == "__main__":
    unittest.main()
