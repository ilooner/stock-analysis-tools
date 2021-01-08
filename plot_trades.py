import click
import pandas as pd
import plotly.express as px

@click.command()
@click.argument('source')
def main(source):
    df = pd.read_csv(source)
    df['timestampNano'] = df['timestampNano'].transform(lambda ts: pd.to_datetime(ts, unit='ns', origin='unix'))
    fig = px.scatter(df, x="timestampNano", y="price")
    fig.show()

if __name__ == "__main__":
    main()
