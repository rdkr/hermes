from datetime import datetime

from datetimerange import DateTimeRange
from pytest import mark

from scheduler.scheduler import filter_times, find_times

SCENARIO_0 = (
    {
        "neel": [DateTimeRange("2020-05-22T10:00:00", "2020-05-22T15:00:00"),],
        "jon": [DateTimeRange("2020-05-22T10:00:00", "2020-05-22T14:00:00"),],
        "liam": [DateTimeRange("2020-05-22T13:00:00", "2020-05-22T16:00:00"),],
    },
    {
        frozenset({"jon", "neel"}): [
            DateTimeRange("2020-05-22T10:00:00", "2020-05-22T14:00:00")
        ],
        frozenset({"neel", "liam"}): [
            DateTimeRange("2020-05-22T13:00:00", "2020-05-22T15:00:00")
        ],
        frozenset({"jon", "liam"}): [
            DateTimeRange("2020-05-22T13:00:00", "2020-05-22T14:00:00")
        ],
        frozenset({"jon", "neel", "liam"}): [
            DateTimeRange("2020-05-22T13:00:00", "2020-05-22T14:00:00")
        ],
    },
)

SCENARIO_1 = (
    {
        "neel": [
            DateTimeRange("2020-05-22T12:00:00", "2020-05-22T16:00:00"),  # 22
            DateTimeRange("2020-05-22T18:00:00", "2020-05-22T22:00:00"),  # 22
            DateTimeRange("2020-05-23T12:00:00", "2020-05-23T16:00:00"),  # 23
            DateTimeRange("2020-05-23T17:00:00", "2020-05-23T21:00:00"),  # 23
        ],
        "sam": [
            DateTimeRange("2020-05-22T17:00:00", "2020-05-22T19:00:00"),  # 22
            DateTimeRange("2020-05-23T12:00:00", "2020-05-23T16:00:00"),  # 23
            DateTimeRange("2020-05-23T19:00:00", "2020-05-23T22:00:00"),  # 23
        ],
        "jon": [
            DateTimeRange("2020-05-22T12:00:00", "2020-05-22T22:00:00"),  # 22
            DateTimeRange("2020-05-23T12:00:00", "2020-05-23T16:00:00"),  # 23
            DateTimeRange("2020-05-23T17:00:00", "2020-05-24T00:00:00"),  # 23
        ],
    },
    {
        frozenset({"neel", "jon"}): [
            DateTimeRange("2020-05-22T12:00:00", "2020-05-22T16:00:00"),  # 22
            DateTimeRange("2020-05-22T18:00:00", "2020-05-22T22:00:00"),  # 22
            DateTimeRange("2020-05-23T12:00:00", "2020-05-23T16:00:00"),  # 23
            DateTimeRange("2020-05-23T17:00:00", "2020-05-23T21:00:00"),  # 23
        ],
        frozenset({"sam", "jon"}): [
            DateTimeRange("2020-05-22T17:00:00", "2020-05-22T19:00:00"),  # 22
            DateTimeRange("2020-05-23T12:00:00", "2020-05-23T16:00:00"),  # 23
            DateTimeRange("2020-05-23T19:00:00", "2020-05-23T22:00:00"),  # 23
        ],
        frozenset({"neel", "sam"}): [
            DateTimeRange("2020-05-22T18:00:00", "2020-05-22T19:00:00"),  # 22
            DateTimeRange("2020-05-23T12:00:00", "2020-05-23T16:00:00"),  # 23
            DateTimeRange("2020-05-23T19:00:00", "2020-05-23T21:00:00"),  # 23
        ],
        frozenset({"jon", "sam", "neel"}): [
            DateTimeRange("2020-05-22T18:00:00", "2020-05-22T19:00:00"),  # 22
            DateTimeRange("2020-05-23T12:00:00", "2020-05-23T16:00:00"),  # 23
            DateTimeRange("2020-05-23T19:00:00", "2020-05-23T21:00:00"),  # 23
        ],
    },
)


@mark.parametrize("times,expected", [SCENARIO_0, SCENARIO_1])
def test_find_times(times, expected):
    actual = dict(find_times(times, 2, datetime(2020, 5, 21)))
    assert actual == expected


@mark.parametrize(
    "times,duration,expected",
    [
        (
            SCENARIO_0[1],
            1.5,
            {
                frozenset({"jon", "neel"}): [
                    DateTimeRange("2020-05-22T10:00:00", "2020-05-22T14:00:00")
                ],
                frozenset({"neel", "liam"}): [
                    DateTimeRange("2020-05-22T13:00:00", "2020-05-22T15:00:00")
                ],
            },
        ),
        (
            SCENARIO_1[1],
            4,
            {
                frozenset({"neel", "jon"}): [
                    DateTimeRange("2020-05-22T12:00:00", "2020-05-22T16:00:00"),  # 22
                    DateTimeRange("2020-05-22T18:00:00", "2020-05-22T22:00:00"),  # 22
                    DateTimeRange("2020-05-23T12:00:00", "2020-05-23T16:00:00"),  # 23
                    DateTimeRange("2020-05-23T17:00:00", "2020-05-23T21:00:00"),  # 23
                ],
                frozenset({"neel", "sam"}): [
                    DateTimeRange("2020-05-23T12:00:00", "2020-05-23T16:00:00"),  # 23
                ],
                frozenset({"sam", "jon"}): [
                    DateTimeRange("2020-05-23T12:00:00", "2020-05-23T16:00:00"),  # 23
                ],
                frozenset({"jon", "sam", "neel"}): [
                    DateTimeRange("2020-05-23T12:00:00", "2020-05-23T16:00:00"),  # 23
                ],
            },
        ),
    ],
)
def test_filter_times(times, duration, expected):
    actual = dict(filter_times(times, duration))
    assert actual == expected
