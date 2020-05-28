def format_datetimeranges(datetimeranges):
    return [f" • {format_range(datetimerange)}\n" for datetimerange in datetimeranges]


def format_timeranges(timeranges):
    return [
        f" • `{timerange.id:03}` {format_range(timerange.datetimerange())}\n"
        for timerange in timeranges
    ]


def format_range(timerange):

    timerange.start_time_format = "%a"
    day = timerange.get_start_time_str()

    timerange.start_time_format = "%d"
    date = timerange.get_start_time_str()
    date_suffix = (
        "th"
        if 11 <= int(date) <= 13
        else {1: "st", 2: "nd", 3: "rd"}.get(int(date) % 10, "th")
    )

    timerange.start_time_format = "%H:%M"
    timerange.end_time_format = "%H:%M (%Z)"
    time_start = timerange.get_start_time_str()
    time_end = timerange.get_end_time_str()

    return f"{day} {date}{date_suffix} @ {time_start} - {time_end}"
