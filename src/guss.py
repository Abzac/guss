import datetime
import hashlib
import random
from typing import Optional


__all__ = [
    'get_credit',
    'get_time_stable_randomized_credit',
]


def get_credit(
    user_name: str, *,
    num_bytes: int = 4,
    min_num: float = 60,
    max_num: float = 100,
    dim: int = 2,
    salt: str = 'Nnfj302b3inr',
) -> float:
    h = hashlib.sha3_256((user_name + salt).encode('utf-8'))
    b = h.digest()

    n = sum([b[i] for i in range(num_bytes)])

    max_sum = 256 * num_bytes
    width: float = max_num - min_num
    normalized_n = n / max_sum
    result = normalized_n * width + min_num

    result = round(result, dim)
    if int(result) == result:
        result = int(result)

    return result


def get_time_stable_randomized_credit(
    user_name: str, *,
    dt: Optional[datetime.datetime],
    hour_threshold: int = 19,
    minute_threshold: int = 37,
    base_credit_min: float = 60,
    base_credit_max: float = 100,
    day_credit_min: float = -30,
    day_credit_max: float = 30,
    hour_credit_min: float = -5,
    hour_credit_max: float = 5,
    random_part_min: int = -2,
    random_part_max: int = 2,
) -> float:
    if dt is None:
        dt = datetime.datetime.now()

    day = dt.day
    hour = dt.hour

    if dt.hour > hour_threshold:
        day += 1

    if dt.minute > minute_threshold:
        hour += 1
        if hour > 23:
            hour = 23

    base_credit = get_credit(
        user_name, min_num=base_credit_min, max_num=base_credit_max,
    )
    day_credit = get_credit(
        str(day), min_num=-day_credit_min, max_num=day_credit_max,
    )
    hour_credit = get_credit(
        str(hour), min_num=-hour_credit_min, max_num=hour_credit_max,
    )
    random_part: int = random.randrange(-random_part_min, random_part_max)

    result: float = base_credit + day_credit + hour_credit + random_part
    result = max(0., result)
    result = min(100., result)

    result = round(result, 2)
    if int(result) == result:
        result = int(result)

    return result
