import my_utils as mu
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--file_name',
                    type=str,
                    required=True,
                    help='CSV file name')
parser.add_argument('--county_column',
                    type=int,
                    required=True,
                    help='Index of the country column')
parser.add_argument('--forestFires_column',
                    type=str,
                    required=True,
                    help='Name of the column')
parser.add_argument('--country',
                    type=str,
                    required=True,
                    help='Country name')

args = parser.parse_args()

file_name = args.file_name
county_column = args.county_column
country = args.country
forestFires_column = args.forestFires_column

def main():
    if county_column != 0:
        raise ValueError("county_column must be 0")

    forestFires = mu.get_column(file_name,
                                county_column,
                                country,
                                forestFires_column)
    print(forestFires)

if __name__ == "__main__":
    main()