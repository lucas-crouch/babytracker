import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#writing simple text
growth = pd.read_csv("csv/Kosmo Emery Crouch_growth.csv")
formula = pd.read_csv("csv/Kosmo Emery Crouch_formula.csv")
pumped = pd.read_csv("csv/Kosmo Emery Crouch_pumped.csv")


st.text("This is the growth and development data for Kosmo Emery Crouch")

growth["kg"] = growth["Weight"].apply(lambda x: float(x[:-3]))
growth["Time"] = growth["Time"].apply(lambda x: datetime.strptime(x[:-7], '%Y/%m/%d'))
growth.drop(growth[growth["kg"] == 0].index, inplace = True)


fig, ax = plt.subplots()
plt.style.use("fivethirtyeight")
plt.figure(figsize=(20, 10))
plt.xlabel("Date")
plt.ylabel("Weight kg")
plt.title("Sample Time Series Plot")
ax.plot(growth["Time"], growth["kg"])
st.pyplot(fig)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = "Formula", "Moma's Milk"
sizes = formula["Amount (ml)"].sum(
), pumped["Amount (ml)"].sum()

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
