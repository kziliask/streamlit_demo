import streamlit as st
import pandas as pd
import altair as alt

st.title("Sales Data Analysis")
brush = alt.selection_interval()
csv = st.file_uploader("Upload CSV", type=["csv"])
if csv is not None:
    df = pd.read_csv(csv)
    source = df
else:
    df = pd.read_csv("data/frozen_yogurt_sales.csv")
source = df
source.time = (
    pd.to_datetime(source.time, format="%H:%M").dt.hour
    + pd.to_datetime(source.time, format="%H:%M").dt.minute / 60
)
source.sale_amount = source.sale_amount.astype(float)
source.flavor = source.flavor.astype(str)
if st.button("Show Data"):
    points = (
        alt.Chart(source)
        .mark_point()
        .encode(
            x="time:Q",
            y=alt.Y(
                "sale_amount:Q",
                scale=alt.Scale(
                    domain=[df.sale_amount.min() - 0.5, df.sale_amount.max() + 0.5]
                ),
            ),
            color=alt.when(brush).then("flavor:N").otherwise(alt.value("lightgray")),
        )
        .add_params(brush)
    )

    bars = (
        alt.Chart(source)
        .mark_bar()
        .encode(y="flavor:N", color="flavor:N", x="count(flavor):Q")
        .transform_filter(brush)
    )

    st.altair_chart(points & bars)
