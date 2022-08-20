import sys
from Util import *


if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    if "--get-data" in sys.argv:
        get_times()
        # for i, arg in sys.argv:
        #     print(f"Argument {i:>6}: {arg}")
