import click
import pandas as pd
import plotly.express as px

@click.command()
@click.argument('source')
def main(source):
    df = pd.read_csv(source)
    df['timestamp'] = df['timestamp'].transform(lambda ts: pd.to_datetime(ts, unit='ms', origin='unix'))
    fig = px.line(df, x='timestamp', y="average")
    fig.show()

if __name__ == "__main__":
    main()
