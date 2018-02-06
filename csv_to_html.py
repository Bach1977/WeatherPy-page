import pandas as pd

df = pd.read_csv("WeatherData.csv")
df.head()

print(df.to_html())