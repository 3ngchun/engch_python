# engch_python
methods that I edited/found useful and want to keep for easy reusing
# How to use: 
```
import Engch as ec;
```
## class Pandaslibrary:
Welcome to Engch's Pandas Library
```
engch_pandas_lib = ec.Pandaslibrary()
df = pd.read_csv(file_name)
```
### def get_csv_header_only(self, file_name):
```
df_header = ec.get_csv_header_only("file_name")
```
### def last_day_of_month(self, dt_date):
```
current_date = datetime.date(int year, int month, int day) 
last_day_of_the_month = ec.last_day_of_month(current_date) 
```
### def df_sort_by_month(self, data_frame, col_date_header_name):
```
dt_dates = ec.df_sort_by_month(df, "column header named: date")
```
### def simplified_by_end_of_month(self, data_frame, df_dates):
``` 
simplified_df = ec.simplified_by_end_of_month(df, dt_dates)
```
## class TimerLibrary: 
Welcome to Engch's Timer Library
```
engch_timer_lib = ec.TimerLibrary()
```
### def time(self):
```
start = engch_timer_lib.time()
# toDo codes..
end = engch_timer_lib.time()
print(end - start)
```
### def time_ns(self):
```
start = engch_timer_lib.time_ns()
# toDo codes..
end = engch_timer_lib.time_ns()
print(end - start)
```
### def sleep(self, duration):
```
engch_timer_lib.sleep(int seconds)
```
## class Library:
Welcome to Engch's Library
```
import Engch as ec;
engch_lib = ec.Library()
```

