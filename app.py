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

@app.route("/show_title/<title>")
def findMovie(title):

    session = Session(engine)
    results = session.query(netflixDB).filter(netflixDB.show_title==title).all()
    session.close

    toReturn=[]
    for movie in results:
        movieDict={"id":movie.show_id,
        "type":movie.show_type,
        "title":movie.show_title,
        "director":movie.show_director,
        "cast":movie.show_cast,
        "country":movie.show_country,
        "date added":movie.date_added,
        "date released":movie.release_year,
        }
        toReturn.append(movieDict)
    return jsonify(toReturn)

@app.route("/director_name/<director>")
def findDirector(director):

    session = Session(engine)
    results = session.query(netflixDB).filter(director in netflixDB.show_director).all()
    session.close

    toReturn=list(np.ravel(results))
    return jsonify(toReturn)

if __name__ == '__main__':
    app.run(debug=True)