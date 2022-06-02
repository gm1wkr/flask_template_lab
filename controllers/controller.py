from flask import render_template, request
from app import app
from models.event_list import *
from models.event import Event

@app.route("/events")
def get_events():
    # events.sort(key=lambda date: datetime.strptime(date, "%d-%b-%y"))
    return render_template("index.html", title="Events Planner", events=events)

@app.route("/events", methods=["POST"])
def add_event():
    
    date = request.form['date']
    name = request.form['name']
    guest_number = request.form['guest_number']
    room_location = request.form['room_location']
    description = request.form['description']
    event_repeats = request.form['event_repeats']
    new_event = Event(date, name, guest_number, room_location, description, event_repeats)
    add_new_event(new_event)
    return render_template("index.html", title="Events Planner", events=events)



