# %%
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

for dirname, _, filenames in os.walk("../data"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df_item = pd.read_csv("../data/olist_order_items_dataset.csv")
df_reviews = pd.read_csv("../data/olist_order_reviews_dataset.csv")
df_orders = pd.read_csv("../data/olist_orders_dataset.csv")
df_products = pd.read_csv("../data/olist_products_dataset.csv")
df_geolocation = pd.read_csv("../data/olist_geolocation_dataset.csv")
df_sellers = pd.read_csv("../data/olist_sellers_dataset.csv")
df_order_pay = pd.read_csv("../data/olist_order_payments_dataset.csv")
df_customers = pd.read_csv("../data/olist_customers_dataset.csv")
df_category = pd.read_csv("../data/product_category_name_translation.csv")

# %%
df_train = df_orders.merge(df_item, on="order_id", how="left")
df_train = df_train.merge(df_order_pay, on="order_id", how="outer", validate="m:m")
df_train = df_train.merge(df_reviews, on="order_id", how="outer")
df_train = df_train.merge(df_products, on="product_id", how="outer")
df_train = df_train.merge(df_customers, on="customer_id", how="outer")
df_train = df_train.merge(df_sellers, on="seller_id", how="outer")
