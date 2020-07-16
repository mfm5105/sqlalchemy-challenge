## SQLAlchemy Homework-Surf's Up

# Dependencies
-%matplotlib inline
-from matplotlib import style
-style.use('fivethirtyeight')
-import matplotlib.pyplot as plt
-import numpy as np
-import pandas as pd
-import datetime as dt

-import sqlalchemy
-from sqlalchemy.ext.automap import automap_base
-from sqlalchemy.orm import Session
-from sqlalchemy import create_engine, func, -inspect

-from flask import Flask, jsonify

## Climate Analysis and Exploration

# Observations

1. Highest Precipitation time over 12 months is in August
2. Most active station is called USC00519281, 2772
3. My trip dates 2016-08-02 and 2016-08-09 had a temperature summary of :
-Min:72
-Average:78
-Max: 83

## Graphs
Precipitation Data over 12 months
Temperature Data over 12 months

## Creating a Flask
Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

* Use Flask to create your routes.

### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.
  
  * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.