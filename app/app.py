import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from datetime import date
from utils.model_utils import fetch_data, train_and_predict, plot_close_price, plot_moving_avg
st.title("📈 Stock Market Price Prediction")

ticker = st.text_input("Enter Ticker Symbol", "AAPL")
start = st.date_input("Start Date", date(2020, 1, 1))
end = st.date_input("End Date", date.today())

# if st.button("Predict"):
#     df = fetch_data(ticker, start, end)
#     st.subheader("📉 Closing Price")
#     st.plotly_chart(plot_close_price(df))

#     prediction = train_and_predict(df)
#     st.success(f"Predicted Close Price for Tomorrow: ${prediction[0]:.2f}")
ma_window = st.slider("Moving Average Window (days)", min_value=5, max_value=100, value=20)


if st.button("Predict"):
    df = fetch_data(ticker, start, end)
    st.plotly_chart(plot_moving_avg(df, window=ma_window))
    st.subheader("📉 Closing Price")
    st.plotly_chart(plot_close_price(df))

    st.subheader("📊 Moving Average Chart")
    st.plotly_chart(plot_moving_avg(df, window=20))  # You can make window size adjustable

    prediction = train_and_predict(df)
    st.success(f"Predicted Close Price for Tomorrow: ${prediction[0]:.2f}")
