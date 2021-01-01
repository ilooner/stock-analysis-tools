import csv
import click

@click.command()
@click.argument('source')
def main(source):
    with open(source, newline='') as csvfile:
        aggregateReader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in aggregateReader:
            print(', '.join(row))

if __name__ == "__main__":
    main()
