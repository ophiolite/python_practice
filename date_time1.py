import datetime

def count_days(d):
    if d == datetime.datetime.today():
        return 'Today is the day'
    if d <= datetime.datetime.today():
        return 'The day is in the past!'
    else:
        time1 = d - datetime.datetime.today()
        time2 = float(time1.days)
        return '%s days' %time2


if __name__ == '__main__':
    d = datetime.datetime(2016,12,24, 18, 0)
    count_days(d)
