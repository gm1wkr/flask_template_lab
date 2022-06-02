from models.event import *

event1 = Event("23/11/2020", "Python Workshop", 8, "Dundee", "Python coding event in Dundee", True)
event2 = Event("10/10/2020", "Brenda's Birthday", 25, "Perth", "Big Brenda's 40th birthday party", False)
event3 = Event("11/12/2020", "Party", 3, "Room 4", "Party Time!", False)
event4 = Event("31/12/2020", "New Year", 100, "Edinburgh", "Happy New Year!", True)
events = [event1, event2, event3, event4]

def add_new_event(event):
  events.append(event)