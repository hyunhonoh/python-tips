# -*- coding: utf-8 -*-
# 여러 시간 
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta

today = date.today()    # 오늘
end_day = date.today() + relativedelta(day=31) # 이번달 마지막날
month_day = date.today() + relativedelta(months=1) - timedelta(days=1) # 오늘 부터 한달
next_first_day = today.replace(day=1) + relativedelta(months=1) # 다음달 1일
next_last_day = next_first_day + relativedelta(day=31)          # 다음달 마지막날
next_first_day = next_first_day.strftime("%Y-%m-%d")
next_last_day = next_last_day.strftime("%Y-%m-%d")
today_day = today.strftime("%Y-%m-%d")
end_day = end_day.strftime("%Y-%m-%d")
month_day = month_day.strftime("%Y-%m-%d")
