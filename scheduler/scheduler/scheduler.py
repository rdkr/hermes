from collections import defaultdict
from datetime import datetime, timedelta
from itertools import combinations
from typing import Dict, FrozenSet, List, Set

from datetimerange import DateTimeRange
from pytz import timezone

MINUTES = 15


def merge_schedules(
    players: Dict[str, List[DateTimeRange]], required: int, start: datetime
) -> Dict[datetime, List[Set[str]]]:
    """Merge individual schedules to time slots where people are free.

    Takes a mapping of people's availability and returns a mapping of
    blocks of time (by the start time) to players free in that block.

    E.g. if Jon is free at 12-2pm and Neel is free from 1-2pm and blocks
    are 30 minutes, then return a dictionary of 4 times, with the first
    2 time blocks mapping to (Jon) and the second two to (Jon, Neel).
    """
    if not start:
        start = datetime.now(timezone("Europe/London")).replace(
            minute=0, second=0, microsecond=0
        )
    candidates = DateTimeRange(start, start + timedelta(days=7))

    potentials = defaultdict(list)

    for candidate_times in candidates.range(timedelta(minutes=MINUTES)):
        candidate_players = []
        for player, timeranges in players.items():
            for timerange in timeranges:
                if timerange.start_datetime <= candidate_times < timerange.end_datetime:
                    candidate_players.append(player)

        for combination_length in range(required, len(candidate_players) + 1):
            combos = combinations(candidate_players, combination_length)
            potentials[candidate_times].extend(combos)

    return potentials


def find_times(
    players: Dict[str, List[DateTimeRange]], required: int, start=None
) -> Dict[FrozenSet[str], List[DateTimeRange]]:

    schedules = merge_schedules(players, required, start)
    potentials = defaultdict(list)

    for viable_time, player_sets in schedules.items():
        for player_set in player_sets:

            current_players = frozenset(player_set)
            if len(current_players) < required:
                continue

            if not potentials[current_players]:
                potentials[current_players].append(DateTimeRange(viable_time))

            current_time = potentials[current_players][-1]

            if (
                viable_time - current_time.start_datetime
            ).total_seconds() <= MINUTES * 60:
                current_time.set_end_datetime(viable_time)
            elif (
                viable_time - current_time.end_datetime
            ).total_seconds() <= MINUTES * 60:
                current_time.set_end_datetime(viable_time)
            else:
                potentials[current_players].append(DateTimeRange(viable_time))

    for time_ranges in potentials.values():
        for time_range in time_ranges:
            time_range.set_end_datetime(
                time_range.end_datetime + timedelta(minutes=MINUTES)
            )

    return potentials


def filter_times(potentials, duration):

    filtered = defaultdict(list)

    for players, time_ranges in potentials.items():
        for time_range in time_ranges:
            if time_range.get_timedelta_second() >= duration * 60 * 60:
                filtered[players].append(time_range)

    return filtered


def deduplicate_times(potentials):

    sorted_result = defaultdict(list)

    for players in sorted(potentials, key=len, reverse=True):
        for times in potentials[players]:
            skip = False
            for already_people, already_times in sorted_result.items():
                for already_time in already_times:
                    if times in already_time and players.issubset(already_people):
                        skip = True
            if not skip:
                sorted_result[players].append(times)

    return sorted_result
