import os

import matplotlib.pyplot as plt
import numpy as np
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

# Times with a power point score of 1000 for an 18 year old male
# From https://www.usaswimming.org/times/popular-resources/power-point-calculator
base_times = {
    150: 18.94,
    1100: 42.03,
    1200: 92.93,
    1500: 251.50,
    2100: 46.65,
    3100: 52.50,
    4100: 46.02,
    5200: 101.95
}


def get_times() -> None:
    """Download times from swimcloud.com and save them to .csv files in times/<team>/<event>.csv"""
    print("Downloading times from swimcloud.com...")
    print("Saving times to times/<team>/<event>.csv")
    for team_code, team_name in team_codes.items():
        team_dir = f"times/{team_name.lower().replace(' ', '_')}"
        print(f"{team_name}...")

        if not os.path.exists(team_dir):
            os.mkdir(team_dir)

        for event_code, event_name in event_codes.items():
            filename = f"{team_dir}/{event_name.lower().replace(' ', '_')}.csv"
            print(f"\t{event_name}")

            # Store data as df
            df = pd.read_html(
                f"https://www.swimcloud.com/team/{team_code}/times/?page=1&gender=M&event={event_code}&course=Y&season=25")[0]
            # Remove other columns
            df = df[['Name', 'Name.1', 'Time']]
            df = df.rename(columns={'Name': 'Rank', 'Name.1': 'Name'})

            # Add power points to individual events only
            if event_code not in [6200, 6400, 7200]:
                df['Points'] = [points(df['Time'][i], event_code)
                                for i in range(len(df))]

            df.to_csv(filename, index=False)


def time_to_seconds(time: str) -> float:
    """Return time in seconds, rounded to two decimal places."""
    try:
        return round(float(time), 2)
    except ValueError:
        return round(int(time[:time.index(":")]) * 60 + float(time[time.index(":") + 1:]), 2)


def time_to_string(time: float) -> str:
    if time < 60:
        return str(time)
    else:
        return f"{int(time / 60)}:{round(time % 60, 2)}"


def points(time: float, event: int) -> int:
    """Return power points for a time in a certain event."""
    return int(1000 * (base_times[event] / time_to_seconds(time)) ** 3)
