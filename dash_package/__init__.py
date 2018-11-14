from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dash

server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///basketball.db'
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
server.config["SQLALCHEMY_ECHO"] = True

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

db = SQLAlchemy(server)

app = dash.Dash(__name__, server=server, url_base_pathname='/dashboard/', external_stylesheets=external_stylesheets)
#app2 = dash.Dash(__name__, server=server, url_base_pathname='/dash/', external_stylesheets=external_stylesheets)

#from dash_package.scrape import ListingBuilder, CraigsListScraper, ListingParser
#
#from dash_package.flask_models import *
from dash_package.dashboard import *
from queries import *
#from dash_package.seed import *
