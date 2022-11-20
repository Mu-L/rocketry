
import time
import datetime
from typing import Tuple

from .base import TimePeriod

def get_period_span(period:'TimePeriod', session=None) -> Tuple[datetime.datetime, datetime.datetime]:

    # To prevent circular import
    from rocketry.parse import parse_time

    if period is None:
        return TimePeriod.min, TimePeriod.max
    if isinstance(period, str):
        period = parse_time(period)

    if session is None:
        dt = datetime.datetime.fromtimestamp(time.time())
    else:
        dt = session._get_datetime_now()

    interval = period.rollback(dt)
    start = interval.left
    end = interval.right
    return start, end
