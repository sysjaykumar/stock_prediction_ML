import yfinance as yf
import pandas as pd
from datetime import date
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

def fetch_data(ticker, start, end):
    return yf.download(ticker, start=start, end=end, auto_adjust=True)

def train_and_predict(df):
    df = df.reset_index()
    df['Date'] = df['Date'].map(pd.Timestamp.toordinal)
    X = df[['Date']]
    y = df['Close']
    model = LinearRegression()
    model.fit(X, y)
    next_day = [[date.today().toordinal() + 1]]
    prediction = model.predict(next_day)
    return prediction[0]

def plot_close_price(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price'))
    fig.update_layout(title="Close Price Trend")
    return fig

def plot_moving_avg(df, window=20):
    df['MA'] = df['Close'].rolling(window=window).mean()

    trace_close = go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close Price')
    trace_ma = go.Scatter(x=df.index, y=df['MA'], mode='lines', name=f'{window}-Day MA')

    layout = go.Layout(title=f'{window}-Day Moving Average vs Close Price',
                       xaxis={'title': 'Date'}, yaxis={'title': 'Price'})

    fig = go.Figure(data=[trace_close, trace_ma], layout=layout)
    return fig