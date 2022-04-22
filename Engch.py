import pandas as pd
import datetime as dt


class Pandaslibrary:
    """
    Welcome to Engch's Pandas Library
    """

    def __init__(self):
        """
        Engch's Pandas Library attributes
        """
        self.banner = "Welcome to Engch's Pandas Library"

    def get_csv_header_only(self, file_name):
        """
        get header of csv only \n
        :param file_name: csv file name
        :return: header of csv
        """
        return pd.read_csv(file_name, header=None, nrows=1)

    def last_day_of_month(self, dt_date):
        """
        determine last day of a given month \n
        ref: https://stackoverflow.com/questions/42950/how-to-get-the-last-day-of-the-month \n
        :param dt_date: datetime.date(year, month, day)
        :return: end of month per actual calendar
        """
        next_month = dt_date.replace(day=28) + dt.timedelta(days=4)
        return next_month - dt.timedelta(days=next_month.day)

    def df_sort_by_month(self, data_frame, col_date_header_name):
        """
        sort cvs by year then month (only latest day per month) \n
        ref: https://stackoverflow.com/questions/26646191/pandas-groupby-month-and-year \n
        :param data_frame: df = pd.read_csv(file_name)
        :param col_date_header_name: 'date'
        :return: sort by year, then month with only the last day per month
        """
        data_frame[[col_date_header_name]] = data_frame[[col_date_header_name]].apply(pd.to_datetime)
        return data_frame.groupby([data_frame.date.dt.year, data_frame.date.dt.month])[col_date_header_name].max()

    def simplified_by_end_of_month(self, data_frame, df_dates):
        """
        simplified to end of month only data set \n
        e.g. Pandas(Index=969, date=Timestamp('1993-10-29 00:00:00'), s_0000=nan, s_0001=13.614) \n
        ref: https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas \n
        :param data_frame: pd.read_csv(file_name)
        :param df_dates: engch_pandas_lib.df_sort_by_month(data_frame, "col_header_date")
        :return: simplified data set
        """
        data_set = []
        for row in data_frame.itertuples():
            # Pandas(Index=0, date='1990-01-02', s_0000=nan)
            for end_of_month in df_dates:
                # row[1] = '1990-01-02', end_of_month = '1990-01-31'
                if row[1] == end_of_month:
                    data_set.append(row)
                    break
        return data_set


class Library:
    """
    Welcome to Engch's Library
    """

    def __init__(self):
        """
        Engch's Library attributes
        """
        self.banner = "Welcome to Engch's Library"


if __name__ == '__main__':
    # engch_pandas_lib = Pandaslibrary()
    # engch_lib = Library()
    pass
