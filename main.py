import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecast days")
option = st.selectbox("Select data to view", options=["Temperature", "Sky"])
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2022-10-23", "2022-10-24", "2022-10-25"]
    temperatures = [11, 15, 13]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


dates, temperatures = get_data(days)
figure = px.line(x=dates, y=temperatures,
                 labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
