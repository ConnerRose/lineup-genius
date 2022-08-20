import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

team_codes = {
    3788: "Dewitt",
    3897: "Okemos",
    3791: "East Lansing",
    3967: "Holt",
    3815: "Grand Ledge",
    3929: "Saint Johns",
    3837: "Haslett"
}

event_codes = {
    150: "50 Free",
    1100: "100 Free",
    1200: "200 Free",
    1500: "500 Free",
    2100: "100 Back",
    3100: "100 Breast",
    4100: "100 Fly",
    5200: "200 IM",
    6200: "200 Free Relay",
    6400: "400 Free Relay",
    7200: "200 Medley Relay"
}


def get_times():
    print("Downloading data from swimcloud.com...")
    for team_code, team_name in team_codes.items():
        print(f"{team_name}...")
        if not os.path.exists(f"times/{team_name.lower().replace(' ', '_')}"):
            os.mkdir(f"times/{team_name.lower().replace(' ', '_')}")
        for event_code, event_name in event_codes.items():
            print(f"\t{event_name}")
            df = pd.read_html(
                f"https://www.swimcloud.com/team/{team_code}/times/?page=1&gender=M&event={event_code}&course=Y&season=25")[0]
            filename = f"times/{team_name.lower().replace(' ' , '_')}/{event_name.lower().replace(' ', '_')}.csv"
            df[['Name', 'Name.1', 'Time']].to_csv(
                filename, index=False, header=["Rank", "Name", "Time"])


def time_to_seconds(time: str) -> float:
    try:
        return round(float(time), 2)
    except ValueError:
        return round(int(time[:time.index(":")]) * 60 + float(time[time.index(":") + 1:]), 2)
