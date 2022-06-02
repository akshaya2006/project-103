import pandas as pd
import plotly.express as px

df = pd.read_csv("Covid.csv")
fig = px.line(df, x="data", y="cases", color="Country")
fig.show()
