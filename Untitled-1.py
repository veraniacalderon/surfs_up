
# Import Python dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Dependencies for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import the dependencies for Flask
from flask import Flask, jsonify

# Setting up database
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
# reflect the database:
Base.prepare(engine, reflect=True)

#save our references to each table
Measurement = Base.classes.measurement
Station = Base.classes.measurement
#create a session link from Python to our database
session = Session(engine)

#To define our Flask app
app = Flask(__name__)
# Example.py
#import app
#print("example__name__ = %s", ___name__)
#if __name___ == "__main__":
#     print("example is being run directly.")
# else:
#     print("example is being imported.")

@app.route("/")

def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
flask run
