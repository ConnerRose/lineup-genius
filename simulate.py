from Util import *

dual_meet_individual_scores = {
    1: 6,
    2: 4,
    3: 3,
    4: 2,
    5: 1,
    6: 0
}

dual_meet_relay_scores = {
    1: 8,
    2: 4,
    3: 2,
    4: 0
}

league_meet_individual_scores = {
    1: 20,
    2: 17,
    3: 16,
    4: 15,
    5: 14,
    6: 13,
    7: 12,
    8: 11,
    9: 9,
    10: 7,
    11: 6,
    12: 5,
    13: 4,
    14: 3,
    15: 2,
    16: 1
}

leageu_meet_relay_scores = {
    1: 40,
    2: 34,
    3: 32,
    4: 30,
    5: 28,
    6: 26,
    7: 24,
    8: 22
}


def simulate(teams: list[int], entries: dict[int, dict[int, list[tuple]]]) -> dict[int, int]:
    """Simulates a meet between either 2 teams in a dual meet or all 7 teams in a league championship meet and returns results.\n
    Entries dict should be formatted as follows:\n
    {
        team_code: {
            event_code: [
                (athlete_name, time_in_seconds)
            ]
        }
    }
    """
    points = {team: 0 for team in teams}

    if len(teams) == 2:
        for event_code, event_name in event_codes.items():
            results = []

            for team_code in teams:
                try:
                    for name, time in entries[team_code][event_code]:
                        results.append((team_code, name, time))
                except KeyError:
                    continue

            if not results:
                break

            results.sort(key=lambda x: x[2])

            print(f"\n{event_name} results:")
            for i, result in enumerate(results):
                points_scored = event_points(i + 1, event_code)
                points[result[0]] += points_scored
                print(
                    f"{i + 1}.  {points_scored}  {time_to_string(result[2])}\t{result[1]}\t{team_codes[result[0]]}")

            print(f"\nResults after {event_name}:")
            for team in teams:
                print(f"{team_codes[team]}: {points[team]}")

    elif len(teams) == 7:
        pass


def event_points(place: int, event_code: int):
    if event_code in [6200, 6400, 7200]:
        return dual_meet_relay_scores[place]
    else:
        return dual_meet_individual_scores[place]
