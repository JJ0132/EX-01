import pandas as pd
import numpy as np

df = pd.read_csv("./samples_exercise_1/cafe_nero_sales_data.csv")

df.replace(["ERROR", "UNKNOWN"], np.nan, inplace=True)

maths = ["Quantity", "Price Per Unit", "Total Spent"]

for col in maths:
    df[col] = pd.to_numeric(df[col])
    
df["Payment Method"] = df["Payment Method"].str.lower()
df["Payment Method"] = df["Payment Method"].replace({
    "cahs": "cash",
    "cas": "cash",
    "digitalwallet": "digital wallet"
})

# FORMULA: TOTAL SPENT = QUANTITY * PRICE PER UNIT
df["Total Spent"] = df["Total Spent"].fillna(df["Quantity"] * df["Price Per Unit"])
df["Quantity"] = df["Quantity"].fillna(df["Total Spent"] / df["Price Per Unit"])
df["Price Per Unit"] = df["Price Per Unit"].fillna(df["Total Spent"] / df["Quantity"])

# PRECIOS
precios = {
    "Cake": 3.0, "Coffee": 2.0, "Cookie": 1.0, "Juice": 3.0, "Salad": 5.0, "Sandwich": 4.0, "Smoothie": 4.0, "Tea": 1.5 
}

df['Price Per Unit'] = df['Price Per Unit'].fillna(df['Item'].map(precios))