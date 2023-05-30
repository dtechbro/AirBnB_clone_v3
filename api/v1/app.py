#!/usr/bin/python3
"""This module contains the principal application"""

from models import storage
from api.vi.views import app_views
from flask import Flask, make_response, jsonify
from os import getenv
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
app