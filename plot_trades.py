import click
import pandas as pd
import plotly.express as px

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
    df['totalPrice'] = df['price'] * df['size']
    sdf = df.groupby(pd.Grouper(freq='1Min', offset=0)).sum()
    sdf['avPrice'] = sdf['totalPrice'] / sdf['size']
    fig = px.line(sdf, x=sdf.index, y='avPrice')
    fig.show()

if __name__ == "__main__":
    main()
