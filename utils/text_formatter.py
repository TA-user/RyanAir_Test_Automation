from collections import namedtuple
from datetime import date


class TextFormatter:
    formatted_date_nt = namedtuple('date_namedtuple', 'year, month_number, month_name, day')

    @classmethod
    def date_formatter(cls, date_str: str) -> formatted_date_nt:
        year, month_number, day = date_str.split("-")
        date_obj = date(int(year), int(month_number), int(day))
        month_name = date_obj.strftime("%b")
        return cls.formatted_date_nt(year, month_number, month_name, day)
