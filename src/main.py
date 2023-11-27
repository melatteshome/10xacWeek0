import argparse
from loader import SlackDataLoader
import utils as utils


def main():
    print('hello')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Export Slack history')

    parser.add_argument('--zip', help="Name of a zip file to import")
    args = parser.parse_args()