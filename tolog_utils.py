import dropbox
import os
import sys
import datetime as dt

DateFormat = "%y%m%d"

def validateTologDate(date):
    """
    tologの日付かどうかちゃんと確認するやつ

    Parameters
    ----------
    date : str
        確認する日付

    Returns
    -------
    ok : bool
        okならTrue
    """
    if len(date) is not 6:
        return False
    try:
        dt.datetime.strptime(date, DateFormat)
    except:
        return False
    return True

