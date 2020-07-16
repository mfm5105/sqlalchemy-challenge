# Dependencies
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

#Create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#Reflect Database
Base = automap_base()
Base.prepare(engine, reflect = True)

#Save table references
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """List all routes that are available."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start/<br/>"
        f"/api/v1.0/start_end/<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the JSON representation of your dictionary."""

    print("Received precipitation api request.")
#finding max date
#finding the max data point in the db
#max_date =session.query(Measurement.date).order_by(Measurement.date.desc()).first()
#max date is '2017-08-23'
#calculating the date 1 year ago from the max data point in the db
    precipitation_data = session.query(func.strftime("%Y-%m-%d", Measurement.date), Measurement.prcp).\
    filter(func.strftime("%Y-%m-%d", Measurement.date) >= dt.date(2016,8,23)).all()

    results_dict = {}
    for result in precipitation_data:
        results_dict[result[0]] = result[1]

    return jsonify(results_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""

    print("Received station api request.")

    #query stations list
    stations = session.query(Station.station).all()

    station_list=list(np.ravel(stations))
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of temperature observations for the previous year."""

    print("Received tobs API request.")
#max date is '2017-08-23'
#calculating the date 1 year ago from the max data point in the db
    tobs_data = session.query(func.strftime("%Y-%m-%d", Measurement.date), Measurement.tobs).\
    filter(func.strftime("%Y-%m-%d", Measurement.date) >= dt.date(2016,8,23)).all()

    results_dict = {}
    for result in tobs_data:
        results_dict[result[0]] = result[1]

    return jsonify(results_dict)


@app.route("/api/v1.0/start/<start>")
def start(start=None):
    print("Received start date api request.")

    #max date is '2017-08-23'
    #calculating the date 1 year ago from the max data point in the db

    precipitation_data = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()

    precipitation_list=list(np.ravel(precipitation_data))

    return jsonify(precipitation_list)

@app.route("/api/v1.0/start_end/<start>/<end>")

def start_end(start, end):
    """Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start
    or start-end range."""
    
    print("Received start date and end date.")

    #max date is '2017-08-23'
    #calculating the date 1 year ago from the max data point in the db
    precipitation_data = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all()
    
    precipitation_list=list(np.ravel(precipitation_data))

    return jsonify(precipitation_list)
if __name__ == "__main__":
    app.run(debug = True)