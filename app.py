import os
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from config import Posgres_Pswrd

engine = create_engine(f"postgres://postgres:{Posgres_Pswrd}@localhost:5432/movies_db")

Base = automap_base()
Base.prepare(engine, reflect=True)

netflixDB=Base.classes.netflix_omdb


app = Flask(__name__)



@app.route("/")
def welcome():
    
    return render_template('index.html')

@app.route("/movie_title/<title>")
def findMovie(title):

    session = Session(engine)
    results = session.query(netflixDB).filter(netflixDB.show_title==title).all()
    session.close

    toReturn=list(np.ravel(results))
    return jsonify(toReturn)

@app.route("/director_name/<director>")
def findDirector(director):

    session = Session(engine)
    results = session.query(netflixDB).filter(director in netflixDB.Show_Director).all()
    session.close

    toReturn=list(np.ravel(results))
    return jsonify(toReturn)

if __name__ == '__main__':
    app.run(debug=True)