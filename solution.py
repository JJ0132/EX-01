import pandas as pd
import numpy as np

df = pd.read_csv("./samples_exercise_1/cafe_nero_sales_data.csv")

df.replace(["ERROR", "UNKNOWN"], np.nan, inplace=True)

maths = ["Quantity", "Price Per Unit", "Total Spent"]