import click
import pandas as pd
import plotly.graph_objs as go
import numpy as np

@click.command()
@click.argument('source')
def main(source):
    df = pd.read_csv(source).drop(columns = [
        'originalTradeID',
        'exchangeID',
        'tradeID',
        'correctionIndicator',
        'reportingFacilityID',
        'quoteTimestampNano',
        'sequenceNo',
        'tape'])
    df = df.set_index(['timestampNano'])
    df.index = pd.to_datetime(df.index, unit='ns', origin='unix')
    df = df.tz_localize("UTC")
    df = df.tz_convert("US/Pacific")
    df = df.between_time('6:00', '15:00')

    adf = df.groupby(pd.Grouper(freq='1Min', offset=0)).agg({'price': [np.mean, np.std, np.min, np.max]})
    adf.columns = adf.columns.map('_'.join).str.strip()
    print(adf.head())

    fig = go.Figure([
        go.Scatter(
            name='Average',
            x=adf.index,
            y=adf['price_mean'],
            mode='lines',
            line=dict(color='rgb(31, 119, 180)')),
        go.Scatter(
            name='min',
            x=adf.index,
            y=adf['price_amin'],
            marker=dict(color="#411"),
            line=dict(width=1),
            mode='lines'),
        go.Scatter(
            name='max',
            x=adf.index,
            y=adf['price_amax'],
            marker=dict(color="#141"),
            line=dict(width=1),
            mode='lines')
    ])
    fig.update_layout(
        yaxis_title='Price',
        title='Error bars, min, and max',
        hovermode="x"
    )
    fig.show()

if __name__ == "__main__":
    main()
