from icalendar import Calendar, Event
from datetime import datetime, timedelta

# tomas = "/Users/aikoma/Downloads/ST33760478Fall2023Cal.ics"

def get_ics_info(file) -> tuple:
    with open(tomas) as f:
            cal = Calendar.from_ical(f.read())
    
    all_classes = []

    for event in cal.walk("VEVENT"):
            # pulls course name and section from summary line
            course, rest = event.get("SUMMARY").split("-")
            sec, rest = rest.split(maxsplit=1)

            # vDDDTypes(2023-09-06 16:00:00, Parameters())
            dt_thing = str(event.get("DTSTART"))
            i = dt_thing.find(":")
            starttime = datetime.strptime(dt_thing[i-2:i+3], "%H:%M")

            dur_thing = str(event.get("DURATION"))
            j = dur_thing.find(":")
            dur = dur_thing[j-1:j+3]
            time_change = timedelta(hours=int(dur[0]), minutes =int(dur[2:]))
            endtime = starttime + time_change

            classtime = starttime.strftime("%H:%M") + "-" + endtime.strftime("%H:%M")

            # ok now get the little TuTh thing
            freq = event.get("RRULE")["BYDAY"]

            all_classes.append((course, sec, classtime, freq))
    return all_classes
    

# print(get_ics_info(tomas))

def get_ics_info_w_dt(file) -> tuple:
    with open(tomas) as f:
            cal = Calendar.from_ical(f.read())

    all_classes = []

    for event in cal.walk("VEVENT"):
            # pulls course name and section from summary line
            course, rest = event.get("SUMMARY").split("-")
            sec, rest = rest.split(maxsplit=1)

            # vDDDTypes(2023-09-06 16:00:00, Parameters())
            dt_thing = str(event.get("DTSTART"))
            i = dt_thing.find(":")
            starttime = datetime.strptime(dt_thing[i-2:i+3], "%H:%M")

            dur_thing = str(event.get("DURATION"))
            j = dur_thing.find(":")
            dur = dur_thing[j-1:j+3]
            time_change = timedelta(hours=int(dur[0]), minutes =int(dur[2:]))
            endtime = starttime + time_change

            # ok now get the little TuTh thing
            freq = event.get("RRULE")["BYDAY"]

            all_classes.append((course, sec, starttime, endtime, freq))

    return all_classes

# print(get_ics_info_w_dt(tomas))
