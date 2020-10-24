import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template

engine = create_engine("#")

Base = automap_base()
Base.prepare(engine, reflect=True)

netflixDB=base.classes.netflix_titles


app = Flask(__name__)



@app.route("/")
def welcome():
    
    return render_template('index.html')

@app.route("/movie_title/<title>")
def findMovie(title):

    session = Session(engine)
    results = session.query(netflixDB).filter(netflixDB.Show_Title==title)
    session.close

    return jsonify(results)

@app.route("/director_name/<director>")
def findDirector(director):

    session = Session(engine)
    results = session.query(netflixDB).filter(director in netflixDB.Show_Director)
    session.close

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)