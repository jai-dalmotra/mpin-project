# common/demographics.py

from datetime import datetime

def format_date_parts(date_str: str) -> str:
    """
    Given 'YYYY-MM-DD', return 'MMDD' and 'YYMMDD'
    (last 4 and last 6 digits) for matching.
    """
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%m%d"), dt.strftime("%y%m%d")
    except ValueError:
        return "", ""

def matches_any_date(pin: str, dates: dict, return_keys: bool = False):
    """
    If return_keys=False: return True if pin matches ANY date part.
    If return_keys=True: return list of date keys that matched.
    """
    matched = []
    for key, d in dates.items():
        mmdd, yymmdd = format_date_parts(d)
        if pin == mmdd or pin == yymmdd[-len(pin):]:
            matched.append(key)
    if return_keys:
        return matched
    return bool(matched)
