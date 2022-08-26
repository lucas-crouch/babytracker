import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

#writing simple text

st.text("Hello")
growth = pd.read_csv("Kosmo Emery Crouch_growth.csv")
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
