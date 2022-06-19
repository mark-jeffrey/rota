# make_shifts.py
Automated google calender scheduling of shifts from and excel rota file

## Usage 
Requires enabling google calender API and credentials.json in the current directory. Follow [googles instructions](https://developers.google.com/workspace/guides/auth-overview) on how to do this. 

### Rota excel file
Save the rota excel file in the current directory. The file should have a format like this:

date | person
-|-
dd/mm/yy | shift
dd/mm/yy | shift
dd/mm/yy | shift

### Edit make_shifts.py
Define the user variables:

variable | input
-|-
shift_col | 'person'
date_col | 'date'
location | 'address you want to appear in the created events'
rota_file | 'name of your rota excel file'
calendarID | 'calender_ID@group.calendar.google.com' [find your calender ID](https://docs.simplecalendar.io/find-google-calendar-id/)

Define the shift type dictionaries:

key | variable
-|-
alias | shift
name | name of the created event (e.g. 'Night shift')|

If you need more than 6 shift types, just add these to the 'shift_list' variable.

### Run make_shifts.py
The first time you will be asked to authenticate via google. This will create a token.json in the current directory. Delete this after use if you do not plan to use it again soon as this will expire. Credentials.json file does not need to be refreshed. 

I'd suggest creating a 'test' calender first so the whole calender can be deleted in the event of an error, rather than having to delete a potentially large number of individual events.