import datetime

year = 2026

int_to_weekday = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

int_to_month = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


days = [datetime.datetime(year, 1, 1) + datetime.timedelta(days=i) for i in range(366)]
#days = [day for day in days if day.year == year and day.weekday() in (0, 6)]
formatted = [[day.strftime("%Y-%m-%d"), int_to_weekday[day.weekday()]] for day in days]
print(len(formatted))
print(formatted[:10])

current_month = days[0].month

with open("calendar" + str(year) + ".txt", "w", encoding="utf-8") as f:
    for i in days:
        if i.month != current_month:
            current_month = i.month
            f.write('** ' + i.strftime("%Y-%m") + ' ' + int_to_month[i.month] + "\n")
        f.write('*** ' + i.strftime("%Y-%m-%d") + ' ' + int_to_weekday[i.weekday()] + "\n")
