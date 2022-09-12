import pprint

from Util import *

pp = pprint.PrettyPrinter(indent=2)


def maximize_power_points(team: int, dual_meet=True) -> dict[int, dict[int, list[tuple]]]:
    if dual_meet:
        pass


def best_swims_first(team_code: int, dual_meet=True) -> dict[int, dict[int, list[tuple]]]:
    """Generates a lineup prioritizing entries with the highest point value"""
    times = load_times(team_code)
    combined = pd.DataFrame(columns=['Event', 'Name', 'Time'])
    relays = {event_code: pd.DataFrame(columns=['Name', 'Time']) for event_code in [
        6200, 6400, 7200]}
    for event_code, df in times.items():
        if event_code in [6200, 6400, 7200]:
            print(df.head())
            relays[event_code]
        df = df.drop(columns=['Rank'])
        df.insert(loc=0, column='Event', value=event_code)
        combined = pd.concat([combined, df])
    combined = combined.sort_values(by=['Points'], ascending=False)
    combined = combined.reset_index(drop=True)

    if dual_meet:
        entry_events = {event_code: 0 for event_code in event_codes}
        entry_names = {name: 0 for name in set(combined['Name'])}
        entries = {event_code: [] for event_code in event_codes}

        for _, row in combined.iterrows():
            if sum(entry_events.values()) >= 24:
                break

            event_code = row['Event']
            if entry_events[event_code] >= 3:
                continue

            name = row['Name']
            if entry_names[name] >= 2:
                continue

            time = time_to_seconds(row['Time'])
            points = row['Points']

            entry_events[event_code] += 1
            entry_names[name] += 1
            entries[event_code].append((name, time))

        # for event_code in [6200, 6400, 7200]:
        #     for time in times.items()
        #     entries[event_code]
        pp.pprint(entries)
        return entries
