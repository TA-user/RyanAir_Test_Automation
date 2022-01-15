from collections import namedtuple
from datetime import date, datetime


class TextFormatter:
    formatted_date_nt = namedtuple('date_namedtuple', 'year, month_number, month_name, day')

    @classmethod
    def format_date(cls, date_str: str) -> formatted_date_nt:
        """
        :param date_str: string in format 'year-month-day'
            for example: "2022-12-14"

        :return: named tuple object
            for example: date_namedtuple(year='2022', month_number='12', month_name='Dec', day='14')
        """
        year, month_number, day = date_str.split("-")
        date_obj = date(int(year), int(month_number), int(day))
        month_name = date_obj.strftime("%b")
        return cls.formatted_date_nt(year, month_number, month_name, day)

    @classmethod
    def format_date_time(cls, result_string_format, date_str: str, time_str: str):
        """
        :param date_str: string in format: 'year-month-day'  for example: "2022-12-14"
        :param time_str: string in format: 'hours:minutes'   for example: "8:20"
        :param result_string_format: string for using as argument in datetime.strftime() method
            example: "%d %b %Y, %H:%M"

        :return: String in required format
            for example: 14 Dec 2022, 08:20
        """
        year, month_number, day = date_str.split("-")
        hours, minutes = time_str.split(":")
        date_obj = datetime(int(year), int(month_number), int(day), int(hours), int(minutes))
        return date_obj.strftime(result_string_format)
