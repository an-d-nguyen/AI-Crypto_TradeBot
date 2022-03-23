import argparse
from CoinbaseAPI import CoinbaseAPI

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train", action="store_true")
    args = parser.parse_args()

    if args.train:
        print(">>> T")
