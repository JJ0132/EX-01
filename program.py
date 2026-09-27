import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('cafe_nero_sales_data.csv')
profile = ProfileReport(df, title="Reporte EDA", explorative=True)

profile.to_notebook_iframe()