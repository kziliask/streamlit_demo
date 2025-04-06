import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App title
st.title("Interactive EOQ Model")
st.latex(r"EOQ = \sqrt{\frac{2K\lambda}{H}}")
# Interactive inputs
demand = st.slider("Annual Demand (units)", 100, 10000, 2000)
order_cost = st.slider("Ordering Cost ($ per order)", 10, 500, 50)
holding_cost = st.slider("Holding Cost ($ per unit/year)", 1, 100, 10)

# EOQ calculation
EOQ = np.sqrt((2 * demand * order_cost) / holding_cost)
orders_per_year = demand / EOQ
total_cost = (orders_per_year * order_cost) + ((EOQ / 2) * holding_cost)

# Output results
st.write(f"### Optimal Order Quantity (EOQ): {EOQ:.2f} units")
st.write(f"Number of Orders per Year: {orders_per_year:.2f}")
st.write(f"Total Annual Cost: ${total_cost:.2f}")

# Visualize costs
quantities = np.arange(EOQ / 2, EOQ * 1.5, EOQ / 50)
costs = (demand / quantities) * order_cost + (quantities / 2) * holding_cost

fig, ax = plt.subplots()
ax.plot(quantities, costs, label="Total Cost Curve")
ax.axvline(EOQ, color="red", linestyle="--", label="EOQ")
ax.set_xlabel("Order Quantity")
ax.set_ylabel("Annual Cost ($)")
ax.legend()
st.pyplot(fig)
