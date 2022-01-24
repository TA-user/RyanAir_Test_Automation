from datetime import date, datetime


class TextFormatter:
    @classmethod
    def format_date(cls, result_string_format, date_str: str):
        """
        :param date_str: string in format 'year-month-day'
            for example: "2022-12-14"
        :param result_string_format: string for using as argument in datetime.strftime() method
            example: "%d %b %Y"
        :return: String in required format
            for example: 14 Dec 2022
        """
        year, month_number, day = date_str.split("-")
        date_obj = date(int(year), int(month_number), int(day))
        return date_obj.strftime(result_string_format)

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
