import sys

from simulate import *
from Util import *


def main():
    if "--get-times" in sys.argv:
        get_times()

    teams = [3788, 3929]
    entries = {
        3788: {
            150: [
                ("person1", 25.00),
                ("person2", 30.00),
                ("another", 31.00)
            ],
            1100: [
                ("person1", 55.00),
                ("person2", 56.00),
                ("another", 60.00)
            ]
        },
        3929: {
            150: [
                ("person3", 27.00),
                ("person4", 28.00),
                ("thing1", 29.00)
            ],
            1100: [
                ("person3", 56.00),
                ("person4", 57.00),
                ("thing1", 61.00)
            ]
        }
    }
    simulate(teams, entries)


if __name__ == "__main__":
    main()
