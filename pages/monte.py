import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

generator = np.random.default_rng()

num_days = st.slider("Number of days", 1, 5, 3)
num_group_var = st.segmented_control(
    "Average Group Size",
    options=[1, 2, 3, 4, 5],
)
num_total_groups_var = st.number_input(
    "Total number of groups",
    min_value=10,
    max_value=50,
    value=20,
)
monte_carlo_demand = []
if num_group_var and num_total_groups_var:
    for i in range(1000):
        total_demand = 0
        for i in range(num_days):
            num_groups = generator.poisson(num_total_groups_var)
            num_per_group = generator.geometric(1 / num_group_var, num_groups)
            total_demand += num_per_group.sum()
        monte_carlo_demand.append(total_demand)
    st.write(total_demand)
    color = st.color_picker("Pick A Color", "#0F20E2")

    fig, ax = plt.subplots()
    sns.histplot(monte_carlo_demand, bins=30, kde=True, ax=ax, color=color)
    ax.set_title("Monte Carlo Simulation of Demand")
    ax.set_xlabel("Demand")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
