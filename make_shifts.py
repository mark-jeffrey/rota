# Script to create google calender events for work shifts from and excel file
'''token.json will expire, delete prior to running to re-generate'''

from __future__ import print_function
import datetime as dt
import pandas as pd
from cal_setup import get_calendar_service


def main():
    # Create google calendar events for shifts in an excel rota file

    # DEFINE USER VARIABLES
    shift_col = '<name>'
    date_col = '<date>'
    location = '<address>'
    rota_file = '<rota.xlsx>'
    calendarID = '<calender_ID>@group.calendar.google.com'

    # DEFINE SHIFT TYPES
    # Alias = how the shift appears in shift_col
    # Name = what you want the name of the created events to be for that shift
    shift1 = {'alias': 'A', 'name': 'Day'}
    shift2 = {'alias': 'B', 'name': 'Long Day'}
    shift3 = {'alias': 'C', 'name': 'Night'}
    shift4 = {'alias': 'L', 'name': 'Leave'}
    shift5 = {'alias': 'S', 'name': 'Study Leave'}
    shift6 = {'alias': 'BH', 'name': 'Bank Holiday'}

    # Read rota file and parse dates
    rota = pd.read_excel(rota_file, parse_dates=True,)

    # List of dicts for shift types
    shift_list = [shift1, shift2, shift3, shift4, shift5, shift6]

    # Initialize empty dict for dict of shift dates
    shift_dates = {}

    # Create dict with key as shift name and value as list of dates when this
    # shift occurs
    for shift_type in shift_list:
        shift_dates[shift_type['name']] = rota[date_col][rota[shift_col].str.fullmatch(
            shift_type['alias'], na=False)].astype(str).tolist()

    def create_shift(date, shift):
        # Create a google calendar event on 'date' with name 'shift'
        service = get_calendar_service()

        event = {
            'summary': shift,
            'location': location,
            'start': {
                'date': date,
                'timeZone': 'Europe/London',
            },
            'end': {
                'date': date,
                'timeZone': 'Europe/London',
            },
        }

        event_result = service.events().insert(
            calendarId=calendarID, body=event).execute()
        print(f'Event for {shift} shift created on {date}')

    # tuple unpack shift_dates and iterate through creating calendar events
    for shift, dates in shift_dates.items():
        for date in dates:
            create_shift(date, shift)


if __name__ == '__main__':
    main()
