# coding=utf-8
import datetime, calendar

'''
时间处理
'''

#获取上月 格式化yyyy-mm
def get_last_month():
    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)
    return last_month.strftime("%Y-%m")

#获取上月第一天 PS：month_fist_day存在月-1有问题
def get_month_first_day():
    month_fist_day = datetime.date(datetime.date.today().year, datetime.date.today().month - 1, 1)
    print(datetime.date.today().year)
    print(datetime.date.today().month)
    return month_fist_day

#获取上月最后一天
def get_month_end_day():
    last_month_end_day = datetime.date(datetime.date.today().year, datetime.date.today().month, 1) - datetime.timedelta(
        1)
    return last_month_end_day

#获取当月第一天
def get_cur_month_first_day():
    now_time = datetime.datetime.now()
    month_first_day = now_time.replace(day=1)
    #datetime.date(datetime.date.today().year, datetime.date.today().month, 1)  当月第一天
    return month_first_day.strftime('%Y-%m-%d')

#获取当年截止当前月份的第一天和最后一天
def get_year_months_day():
    result = {}
    # 获取当前年份
    thisYear = datetime.date.today().year
    # 获取当前月份
    thisMonth = datetime.date.today().month
    # 获取当前天
    thisDay = datetime.date.today().day
    for x in range(1, thisMonth + 1):
        monthRange = calendar.monthrange(thisYear, x)[1]
        startDay = str(thisYear) + "-" + str(x).zfill(2) + "-01"
        endDay = str(thisYear) + "-" + str(x).zfill(2) + "-"
        #如果不想本月取最后一天取当前日期，可不做判断，直接用endDay = endDay + str(monthRange).zfill(2)
        if x == thisMonth:
            endDay = endDay + str(thisDay).zfill(2)
        else:
            endDay = endDay + str(monthRange).zfill(2)
        result[str(x)] = [startDay, endDay]
    return result


if __name__ == '__main__':
    print(get_year_months_day())