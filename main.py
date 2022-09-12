import sys

from generator import *
from simulate import *
from Util import *


def main():
    if "--get-times" in sys.argv:
        get_times()

    teams = [3788, 3897]
    entries = {
        3788: best_swims_first(3788),
        3897: best_swims_first(3897)
    }
    simulate(teams, entries)
    # dewitt_times = load_times(3788)
    # print(dewitt_times[2100].head())
    # best_swims_first(3788)


if __name__ == "__main__":
    main()
