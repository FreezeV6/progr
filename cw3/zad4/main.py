import argparse

from cw3.zad4.Brewery.Brewery import function_zad7_8

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--city', type=str, help='City to filter breweries by', required=False)
    args = parser.parse_args()
    function_zad7_8(args.city)
