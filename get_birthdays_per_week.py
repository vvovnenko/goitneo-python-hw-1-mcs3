from datetime import datetime
from collections import defaultdict
import calendar

def get_birthdays_per_week(users) :
    congratulations = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        nex_birthday = user["birthday"].date().replace(year=today.year)

        if (nex_birthday < today):
            nex_birthday = nex_birthday.replace(year=today.year+1)
        
        delta_days = (nex_birthday - today).days

        if delta_days >= 7:
            continue

        weekday = nex_birthday.weekday()
        if weekday in [5, 6]:
            weekday = 0
            
        congratulations[weekday].append(user['name'])

    for weekday, users in congratulations.items():
        print('{}: {}'.format(calendar.day_name[weekday], ', '.join(users)))
