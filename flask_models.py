from dash_package import db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

class Coach(db.Model): #db.Model is the same as Base in original SQL Alchemy
    __tablename__ = 'coach'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    years = db.Column(db.Integer)
    salary = db.Column(db.Float)
    sal_school = db.Column(db.Text)
#     schools = relationship('School', secondary = 'joinedtable')
    schools = db.relationship('School', secondary = 'JoinedTable')
    #back_populates=db.back_populates('coaches'))

class School(db.Model):
    __tablename__ = 'school'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    years = db.Column(db.Text)
    winloss = db.Column(Float)
    team_points = db.Column(Float)
    opp_points = db.Column(Float)
#     coaches = relationship('Coach', secondary = 'joinedtable')
    coaches = db.relationship('Coach', secondary = 'JoinedTable')
    #back_populates=db.back_populates('schools'))

JoinedTable = db.Table('JoinedTable',\
db.Column('school_id', db.Integer, db.ForeignKey('school.id'), primary_key = True),\
db.Column('coach_id', db.Integer, db.ForeignKey('coach.id'), primary_key = True))
