import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/frozen_yogurt_sales.csv")
source = df
source.time = (
    pd.to_datetime(source.time, format="%H:%M").dt.hour
    + pd.to_datetime(source.time, format="%H:%M").dt.minute / 60
)
source.sale_amount = source.sale_amount.astype(float)
source.flavor = source.flavor.astype(str)
print(source.head())
st.write("# Monte Carlo Simulation for EOQ Model")
generator = np.random.default_rng()
customer_rate = st.slider("Customer Rate (units per day)", 1, 100, 10)
group_param = st.selectbox("Average Group Size", [1, 2, 3, 4, 5])
time = st.slider("Time (in days)", 1, 10, 5)
purchase_rate = st.slider("Purchase Rate (units per day)", 0.0, 1.0, step=0.1)
if st.button("Run Simulation"):
    demands = []
    for i in range(1000):
        customer_num = generator.poisson(customer_rate)
        group_size = generator.geometric(1 / group_param, customer_num)
        total_customers = np.sum(group_size)
        total_demand = total_customers * purchase_rate
        demands.append(total_demand)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(demands, bins=30, density=True, alpha=0.6, color="g")
    ax.set_xlabel("Demand")
    ax.set_ylabel("Density")
    ax.set_title("Monte Carlo Simulation of Demand")
    st.pyplot(fig)
